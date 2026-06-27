from pathlib import Path
from sys import argv
from collections import defaultdict

N = 25
N2 = 75

def parse_input(path: Path) -> list[int]:
    line = path.open().readline().strip()
    return [int(x) for x in line.split(" ")]

def solution_star_one(stones: list[int]) -> int:
    local_stones = stones.copy()
    new_stones = []

    for _ in range(N):
        for stone in local_stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:len(str(stone))//2]))
                new_stones.append(int(str(stone)[len(str(stone))//2:]))
            else:
                new_stones.append(stone * 2024)
        
        local_stones = new_stones
        new_stones = []

    return len(local_stones)

def solution_star_two(stones: list[int]) -> int:
    cache = defaultdict(lambda: dict())

    def evolve(stone: int, blink: int = 0) -> int:
        if stone in cache[blink]: return cache[blink][stone]
        if blink == N2: return 1

        new_stones = []
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
        else:
            new_stones.append(stone * 2024)

        cache[blink][stone] = sum(evolve(x, blink + 1) for x in new_stones)
        return cache[blink][stone]

    return sum(evolve(x) for x in stones)

if __name__ == "__main__":
    stones = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(stones))
    print("Solution Star Two:", solution_star_two(stones))
