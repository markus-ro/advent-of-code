from pathlib import Path
from sys import argv

import numpy as np

def parse_input(path: Path) -> np.ndarray[np.uint8]:
    lines = path.read_text().strip().splitlines()
    rows = [np.fromiter((int(ch) for ch in line.strip()), dtype=np.uint8, count=len(line.strip()))
            for line in lines if line.strip()]
    return np.vstack(rows)


def solution_star_one(topographic_map: np.ndarray[np.uint8]) -> None:
    visited = set()
    def climb(position: tuple[int, int], start: int) -> int:
        if not (0 <= position[0] < topographic_map.shape[0]): return
        if not (0 <= position[1] < topographic_map.shape[1]): return
        if topographic_map[position] != start + 1: return
        if topographic_map[position] == 9:
            visited.add(position)
            return

        climb((position[0] + 1, position[1]    ), topographic_map[position])
        climb((position[0] - 1, position[1]    ), topographic_map[position])
        climb((position[0]    , position[1] + 1), topographic_map[position])
        climb((position[0]    , position[1] - 1), topographic_map[position])

    total = 0
    for i in range(topographic_map.shape[0]):
        for j in range(topographic_map.shape[1]):
            if topographic_map[i, j] != 0: continue
            visited = set()
            climb((i, j), - 1)
            total += len(visited)
    return total

def solution_star_two(topographic_map: np.ndarray[np.ndarray[np.uint8]]) -> int:
    cache_map = np.zeros(shape=topographic_map.shape, dtype=np.int8) - 1

    def climb(position: tuple[int, int], start: int) -> int:
        if not (0 <= position[0] < topographic_map.shape[0]): return 0
        if not (0 <= position[1] < topographic_map.shape[1]): return 0
        if topographic_map[position] != start + 1: return 0
        if cache_map[position] > -1: return cache_map[position]
        if topographic_map[position] == 9: return 1

        cache_map[position] = 0
        cache_map[position] += climb((position[0] + 1, position[1]    ), topographic_map[position])
        cache_map[position] += climb((position[0] - 1, position[1]    ), topographic_map[position])
        cache_map[position] += climb((position[0]    , position[1] + 1), topographic_map[position])
        cache_map[position] += climb((position[0]    , position[1] - 1), topographic_map[position])

        return cache_map[position]

    for i in range(topographic_map.shape[0]):
        for j in range(topographic_map.shape[1]):
            if topographic_map[i, j] != 0: continue
            climb((i, j), - 1)
    return np.sum(cache_map[topographic_map == 0])

if __name__ == "__main__":
    topographic_map = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(topographic_map))
    print("Solution Star Two:", solution_star_two(topographic_map))
