from pathlib import Path
from sys import argv
from collections import defaultdict

def parse_input(file: Path) -> tuple[dict[list[int]], list[list[int]]]:
    lines = file.open().read().splitlines()

    ordering = defaultdict(lambda : [])
    updates = []

    # first read ordering
    for i, line in enumerate(lines):
        if line.strip() == "":
            break
        a, b = line.split("|")
        a, b = int(a), int(b)
        ordering[a].append(b)

    # then read updates
    for line in lines[i + 1:]:
        update = list(map(int, line.split(",")))
        updates.append(update)

    return ordering, updates

def solution_star_one(ordering: dict[list[int]], updates: list[list[int]]) -> int:
    def check_update_validity(update: list[int]) -> bool:
        seen = dict()
        for num in update:
            seen[num] = None
            for prev in ordering[num]:
                if prev in seen:
                    return False
        return True
    

    return sum(update[len(update) // 2] for update in updates if check_update_validity(update))

def solution_star_two(ordering: dict[list[int]], updates: list[list[int]]) -> int:
    def check_update_validity(update: list[int]) -> bool:
        seen = dict()
        for num in update:
            seen[num] = None
            for prev in ordering[num]:
                if prev in seen:
                    return False
        return True

    invalid_updates = [update for update in updates if not check_update_validity(update)]

    # fix invalid updates b< reordering
    for update in invalid_updates:
        while not check_update_validity(update):
            for i, a in enumerate(update):
                for j, b in enumerate(update[i + 1:]):
                    if a in ordering[b]: update[i], update[i + 1 + j] = update[i + 1 + j], update[i]

    return sum(update[len(update) // 2] for update in invalid_updates)



if __name__ == "__main__":
    input_file = Path(argv[1])
    ordering, updates = parse_input(input_file)
    print("Solution Star One:", solution_star_one(ordering, updates))
    print("Solution Star Two:", solution_star_two(ordering, updates))