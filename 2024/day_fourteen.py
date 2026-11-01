import re
from pathlib import Path
from sys import argv

import numpy as np

GRID_SIZE = np.array([101, 103])

class Robot:
    def __init__(self, position: np.ndarray, movement: np.ndarray):
        self._position = position
        self._movement = movement

    def position_after(self, ticks: int) -> np.ndarray:
        return (self._position + self._movement * ticks) % GRID_SIZE

    def simulate(self, ticks: int):
        self._position += self._movement * ticks
        self._position %= GRID_SIZE

    def __call__(self, ticks: int):
        self.simulate(ticks)

    @property
    def position(self) -> np.ndarray:
        return self._position

    @property
    def movement(self) -> np.ndarray:
        return self._movement

    def __str__(self) -> str:
        return f"Robot(position={self._position}, movement={self._movement})"


def parse_robots(input_data: list[str]) -> list[Robot]:
    pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")

    robots = []
    for line in input_data:
        match = pattern.match(line)
        if match:
            p_x, p_y, v_x, v_y = map(int, match.groups())
            robots.append(Robot(np.array([p_x, p_y]), np.array([v_x, v_y])))

    return robots

def solution_star_one(robots: list[Robot]) -> int:
    q1, q2, q3, q4 = 0, 0, 0, 0

    for robot in robots:
        pos = robot.position_after(100)

        if pos[0] == GRID_SIZE[0] // 2:
            continue

        if pos[1] == GRID_SIZE[1] // 2:
            continue

        if pos[0] < GRID_SIZE[0] // 2:
            if pos[1] < GRID_SIZE[1] // 2:
                q1 += 1
            else:
                q3 += 1
        else:
            if pos[1] < GRID_SIZE[1] // 2:
                q2 += 1
            else:
                q4 += 1

    return q1 * q2 * q3 * q4


def largest_connected_component(positions: set[tuple[int, int]]) -> int:
    unvisited = positions.copy()
    largest = 0

    while unvisited:
        stack = [unvisited.pop()]
        component_size = 0
        while stack:
            x, y = stack.pop()
            component_size += 1
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    neighbor = (x + dx, y + dy)
                    if neighbor in unvisited:
                        unvisited.remove(neighbor)
                        stack.append(neighbor)
        largest = max(largest, component_size)

    return largest


def solution_star_two(robots: list[Robot]) -> int:
    period = int(GRID_SIZE[0] * GRID_SIZE[1])
    initial_positions = np.array([robot.position for robot in robots])
    movements = np.array([robot.movement for robot in robots])

    best_second = 0
    largest_component = 0
    for second in range(period):
        positions = (initial_positions + movements * second) % GRID_SIZE
        occupied = {tuple(map(int, position)) for position in positions}
        component_size = largest_connected_component(occupied)
        if component_size > largest_component:
            best_second = second
            largest_component = component_size

    return best_second

if __name__ == "__main__":
    input_data: list[str] = Path(argv[1]).open().readlines()
    robots = parse_robots(input_data)
    print("Solution Star One:", solution_star_one(robots))
    print("Solution Star Two:", solution_star_two(robots))
