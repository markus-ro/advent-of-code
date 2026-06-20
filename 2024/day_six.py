from pathlib import Path
from sys import argv
from collections import defaultdict

def parse_input(file: Path) -> tuple[list[list[str]], tuple[int, int]]:
    map = []
    position = None
    with file.open() as f:
        for i, line in enumerate(f.readlines()):
            map.append(list(line.strip()))
            if "^" in line: position = (i, line.index("^"))

    return map, position
    
def solution_star_one(map: list[list[str]], start_position: tuple[int, int]) -> dict[tuple[int, int], tuple[int, int]]:
    def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
        return (direction[1], -direction[0])

    direction = (-1, 0)
    positions = {start_position: direction}

    while True:
        next_position = (start_position[0] + direction[0], start_position[1] + direction[1])
        if next_position[0] < 0 or next_position[0] >= len(map) or next_position[1] < 0 or next_position[1] >= len(map[0]):
            break
        elif map[next_position[0]][next_position[1]] == "#":
            direction = turn_right(direction)
        elif map[next_position[0]][next_position[1]] in [".", "^"]:
            start_position = next_position
            positions[start_position] = direction
        else:
            break
        
    return positions

def solution_star_two(map: list[list[str]], start_position: tuple[int, int]) -> int:
    def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
        return (direction[1], -direction[0])

    def check_for_circle(obstruction_pos: tuple[int, int]) -> bool:
        position = start_position
        direction = (-1, 0)
        visited_states = set()
        
        while True:
            state = (position, direction)
            if state in visited_states:
                return True
            visited_states.add(state)
            
            next_position = (position[0] + direction[0], position[1] + direction[1])
            if next_position[0] < 0 or next_position[0] >= len(map) or next_position[1] < 0 or next_position[1] >= len(map[0]):
                return False
            elif map[next_position[0]][next_position[1]] == "#" or next_position == obstruction_pos:
                direction = turn_right(direction)
            else:
                position = next_position

    visited_positions = solution_star_one(map, start_position)
    circles = 0
    
    for position in visited_positions.keys():
        if position != start_position:
            if check_for_circle(position):
                circles += 1

    return circles

if __name__ == "__main__":
    map, position = parse_input(Path(argv[1]))
    print("Solution Star One:", len(solution_star_one(map, position)))
    print("Solution Star Two:", solution_star_two(map, position))