from pathlib import Path
from sys import argv

def parse_input(path: Path) -> list[list[str]]:
    return [list(x.rstrip("\n")) for x in path.open().read().splitlines()]

def solution_star_one(region: list[list[str]]) -> int:
    region_visited = [x.copy() for x in region]

    def flood(
        position: tuple[int, int], sign: str, out_region: list[tuple[int, int]]
    ) -> int:
        _x, _y = position
        if not 0 <= _x < len(region):
            return 1
        if not 0 <= _y < len(region[_x]):
            return 1

        # position has already been visited
        if region_visited[_x][_y] == ".":
            if region[_x][_y] == sign:
                return 0
            return 1

        # region has not yet been visited but has different sign
        if region[_x][_y] != sign:
            return 1

        # region has not yet been visited but has correct sign
        region_visited[_x][_y] = "."
        out_region.append(position)
        fences = flood((_x - 1, _y), sign, out_region)
        fences += flood((_x + 1, _y), sign, out_region)
        fences += flood((_x, _y + 1), sign, out_region)
        fences += flood((_x, _y - 1), sign, out_region)
        return fences

    total = 0
    for x in range(len(region)):
        for y in range(len(region[0])):
            if region_visited[x][y] != ".":
                new_region: list[tuple[int, int]] = []
                fences = flood((x, y), region_visited[x][y], new_region)
                total += fences * len(new_region)
    return total

def solution_star_two(region: list[list[str]]) -> int:
    pass

if __name__ == "__main__":
    region = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(region))
    print("Solution Star Two:", solution_star_two(region))
