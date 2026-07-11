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

def count_sides(region_cells: set[tuple[int, int]]) -> int:
    """Count the number of sides in a region by counting corners."""
    sides = 0
    
    for x, y in region_cells:
        # Count outer corners (convex): where two perpendicular edges are exposed
        # Top-left outer corner
        if (x - 1, y) not in region_cells and (x, y - 1) not in region_cells:
            sides += 1
        
        # Top-right outer corner
        if (x - 1, y) not in region_cells and (x, y + 1) not in region_cells:
            sides += 1
        
        # Bottom-right outer corner
        if (x + 1, y) not in region_cells and (x, y + 1) not in region_cells:
            sides += 1
        
        # Bottom-left outer corner
        if (x + 1, y) not in region_cells and (x, y - 1) not in region_cells:
            sides += 1
        
        # Count inner corners (concave): where region cells meet at corners but not diagonally
        # Top-left inner corner
        if (
            (x - 1, y) in region_cells
            and (x, y - 1) in region_cells
            and (x - 1, y - 1) not in region_cells
        ):
            sides += 1
        
        # Top-right inner corner
        if (
            (x - 1, y) in region_cells
            and (x, y + 1) in region_cells
            and (x - 1, y + 1) not in region_cells
        ):
            sides += 1
        
        # Bottom-right inner corner
        if (
            (x + 1, y) in region_cells
            and (x, y + 1) in region_cells
            and (x + 1, y + 1) not in region_cells
        ):
            sides += 1
        
        # Bottom-left inner corner
        if (
            (x + 1, y) in region_cells
            and (x, y - 1) in region_cells
            and (x + 1, y - 1) not in region_cells
        ):
            sides += 1
    
    return sides

def solution_star_two(region: list[list[str]]) -> int:
    region_visited = [x.copy() for x in region]

    def flood(
        position: tuple[int, int], sign: str, out_region: list[tuple[int, int]]
    ) -> None:
        _x, _y = position
        if not 0 <= _x < len(region):
            return
        if not 0 <= _y < len(region[_x]):
            return

        # position has already been visited
        if region_visited[_x][_y] == ".":
            return

        # region has different sign
        if region[_x][_y] != sign:
            return

        # region has not yet been visited and has correct sign
        region_visited[_x][_y] = "."
        out_region.append(position)
        flood((_x - 1, _y), sign, out_region)
        flood((_x + 1, _y), sign, out_region)
        flood((_x, _y + 1), sign, out_region)
        flood((_x, _y - 1), sign, out_region)

    total = 0
    for x in range(len(region)):
        for y in range(len(region[0])):
            if region_visited[x][y] != ".":
                new_region: list[tuple[int, int]] = []
                flood((x, y), region_visited[x][y], new_region)
                sides = count_sides(set(new_region))
                total += sides * len(new_region)
    return total

if __name__ == "__main__":
    region = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(region))
    print("Solution Star Two:", solution_star_two(region))
