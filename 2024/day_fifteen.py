from pathlib import Path
from sys import argv

import numpy as np
from numpy.typing import NDArray

Position = NDArray[np.int_]

# movements in row major order (row, column)
MOVEMENTS: dict[str, Position] = {
    "^": np.array([-1, 0]),
    "v": np.array([1, 0]),
    "<": np.array([0, -1]),
    ">": np.array([0, 1]),
}

GRID_SIZE = (50, 50)

def remove(val: np.ndarray, l: list[np.ndarray]) -> None:
    for idx in range(len(l)):
        if np.array_equal(l[idx], val):
            l.pop(idx)
            return


def parse_input(input_data: str) -> tuple[list[Position], list[Position], Position, list[Position]]:
    lines = input_data.splitlines()
    separator = lines.index("")
    grid_lines = lines[:separator]
    move_lines = lines[separator + 1 :]
    grid = np.array([list(line) for line in grid_lines])
    boxes = list(np.argwhere(grid == "O"))
    walls = list(np.argwhere(grid == "#"))
    robot = np.argwhere(grid == "@")[0]
    moves = "".join(move_lines)
    return walls, boxes, robot, moves

def print_grid(walls: list[Position], boxes: list[Position], robot: Position) -> None:
    grid = np.full(GRID_SIZE, ".")
    for wall in walls:
        grid[wall[0], wall[1]] = "#"
    for box in boxes:
        grid[box[0], box[1]] = "O"
    grid[robot[0], robot[1]] = "@"
    print("\n".join("".join(row) for row in grid))

def solution_star_one(
    walls: list[Position], boxes: list[Position], robot: Position, moves: str
) -> int:
    _boxes = [box.copy() for box in boxes]
    _robot = robot.copy()

    def propagate(position: Position, movement: Position) -> bool:
        new_position = position + movement

        if any((new_position == wall).all() for wall in walls):
            return False

        box = next(
            (b for b in _boxes if (new_position == b).all()),
            None,
        )
        if box is not None:
            if not propagate(new_position, movement):
                return False
            remove(box, _boxes)
            _boxes.append(new_position.copy() + movement)

        return True

    for move in moves:
        movement = MOVEMENTS[move]
        if propagate(_robot, movement):
            _robot += movement
            # print_grid(walls, _boxes, _robot)

    return sum(100 * box[0] + box[1] for box in _boxes)


def solution_star_two(
    walls: list[Position], boxes: list[Position], robot: Position, moves: str
) -> int:
    wall_set = {tuple(wall) for wall in walls}
    box_set = {tuple(box) for box in boxes}
    robot_pos = tuple(robot)

    def box_at(cell: tuple[int, int]) -> tuple[int, int] | None:
        r, c = cell
        for left_c in (c, c - 1):
            left = (r, left_c)
            if left in box_set:
                return left
        return None

    for move in moves:
        dr, dc = map(int, MOVEMENTS[move])
        target = (robot_pos[0] + dr, robot_pos[1] + dc)

        if target in wall_set:
            continue

        first_box = box_at(target)
        if first_box is None:
            robot_pos = target
            continue

        moving: set[tuple[int, int]] = set()

        def can_move(box: tuple[int, int]) -> bool:
            if box in moving:
                return True
            moving.add(box)

            r, c = box
            new_left = (r + dr, c + dc)

            for cell in (new_left, (new_left[0], new_left[1] + 1)):
                if cell in wall_set:
                    return False

                other_box = box_at(cell)
                if other_box is not None and other_box != box:
                    if not can_move(other_box):
                        return False

            return True

        if not can_move(first_box):
            continue

        box_set.difference_update(moving)
        box_set.update((r + dr, c + dc) for r, c in moving)
        robot_pos = target

    return sum(100 * r + c for r, c in box_set)


if __name__ == "__main__":
    walls, boxes, robot, moves = parse_input(Path(argv[1]).read_text())
    print_grid(walls, boxes, robot)
    print("Solution Star One:", solution_star_one(walls, boxes, robot, moves))

    wide_walls = [
        np.array([r, 2 * c + offset])
        for wall in walls
        for r, c in [wall]
        for offset in (0, 1)
    ]
    wide_boxes = [np.array([box[0], 2 * box[1]]) for box in boxes]
    wide_robot = np.array([robot[0], 2 * robot[1]])
    
    print("Solution Star Two:", solution_star_two(wide_walls, wide_boxes, wide_robot, moves))