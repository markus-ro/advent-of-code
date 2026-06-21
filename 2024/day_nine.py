from pathlib import Path
from sys import argv


def parse_input(file: Path) -> list[int]:
    return [int(x) for x in list(file.read_text().strip())]

def expand_disk_map(disk_map: list[int]) -> list[int]:
    k = 0
    expanded_disk_map = []
    for i, n in enumerate(disk_map):
        expanded_disk_map += [f"{k}" if i % 2 == 0 else "." for _ in range(n)]
        k += 1 if i % 2 == 0 else 0

    return expanded_disk_map

def solution_star_one(disk_map: list[int]) -> int:
    expanded_disk_map = expand_disk_map(disk_map)
    print("".join(expanded_disk_map))

    left, right = 0, len(expanded_disk_map) - 1
    while left < right:
        if expanded_disk_map[left] == "." and expanded_disk_map[right] != ".":
            expanded_disk_map[left] = expanded_disk_map[right]
            expanded_disk_map[right] = "."
        if expanded_disk_map[left] != ".": left += 1
        if expanded_disk_map[right] == ".": right -= 1

    return sum(int(expanded_disk_map[i]) * i if expanded_disk_map[i] != "." else 0 for i in range(len(expanded_disk_map)))

def solution_star_two(disk_map: list[int]) -> int:
    pass

if __name__ == "__main__":
    disk_map = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(disk_map))
    print("Solution Star Two:", solution_star_two(disk_map))