from pathlib import Path
from sys import argv


def parse_input(file: Path) -> list[int]:
    return [int(x) for x in list(file.read_text().strip())]

def expand_disk_map(disk_map: list[int]) -> tuple[list[int], dict[int, tuple[int, int]], list[tuple[int, int]]]:
    k = 0
    expanded_disk_map = []
    blocks = dict()
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            blocks[k] = (len(expanded_disk_map), n)
            expanded_disk_map += [f"{k}" for _ in range(n)]
            k += 1
        else:
            expanded_disk_map += ["." for _ in range(n)]

    return expanded_disk_map, blocks

def get_blanks(disk_map: list[str]) -> list[tuple[int, int]]:
    blanks = []
    index = 0
    while index < len(disk_map):
        if disk_map[index] == ".":
            start = index
            while index < len(disk_map) and disk_map[index] == ".":
                index += 1
            blanks.append((start, index - start))
        else:
            index += 1
    return blanks

def solution_star_one(disk_map: list[int]) -> int:
    disk_map, _ = expand_disk_map(disk_map)

    left, right = 0, len(disk_map) - 1
    while left < right:
        if disk_map[left] == "." and disk_map[right] != ".":
            disk_map[left] = disk_map[right]
            disk_map[right] = "."
        if disk_map[left] != ".": left += 1
        if disk_map[right] == ".": right -= 1

    return sum(int(disk_map[i]) * i if disk_map[i] != "." else 0 for i in range(len(disk_map)))

def solution_star_two(disk_map: list[int]) -> int:
    disk_map, blocks = expand_disk_map(disk_map)

    for k in range(len(blocks) - 1, -1, -1):
        block_start = blocks[k][0]
        block_length = blocks[k][1]

        blanks = [blank for blank in get_blanks(disk_map) if blank[0] < block_start]
        if not blanks:
            continue

        for blank_start, blank_length in blanks:
            if blank_length >= block_length:
                for j in range(block_length):
                    disk_map[blank_start + j] = f"{k}"
                for j in range(block_length):
                    disk_map[block_start + j] = "."
                break

    return sum(int(disk_map[i]) * i if disk_map[i] != "." else 0 for i in range(len(disk_map)))

if __name__ == "__main__":
    disk_map = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(disk_map))
    print("Solution Star Two:", solution_star_two(disk_map))