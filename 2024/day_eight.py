from pathlib import Path
from sys import argv

def parse_input(file: Path) -> tuple[list[list[str]], dict[str, list[tuple[int, int]]]]:
    city_map = []
    with file.open() as f:
        for line in f.readlines():
            city_map.append(list(line.strip()))

    antennas: dict[str, list[tuple[int, int]]] = {}
    for i in range(len(city_map)):
        for j in range(len(city_map[i])):
            if city_map[i][j] != ".":
                if city_map[i][j] not in antennas:
                    antennas[city_map[i][j]] = []
                antennas[city_map[i][j]].append((i, j))

    return city_map, antennas

def solution_star_one(city_map: list[list[str]], antennas: dict[str, list[tuple[int, int]]]) -> int:
    antinodes = set()
    max_x = len(city_map)
    max_y = len(city_map[0])

    for frequency in antennas:
        for a1 in antennas[frequency]:
            for a2 in antennas[frequency]:
                if a1 == a2: continue
                offset = (a2[0] - a1[0], a2[1] - a1[1])
                antinode = (a1[0] - offset[0], a1[1] - offset[1])
                if 0 <= antinode[0] < max_x and 0 <= antinode[1] < max_y:
                    antinodes.add(antinode)

    return len(antinodes)

def solution_star_two(city_map: list[list[str]], antennas: dict[str, list[tuple[int, int]]]) -> int:
    antinodes = set()
    max_x = len(city_map)
    max_y = len(city_map[0])

    for frequency in antennas:
        if len(antennas[frequency]) < 2:
            continue
        
        for a1 in antennas[frequency]:
            for a2 in antennas[frequency]:
                if a1 == a2: continue
                offset = (a2[0] - a1[0], a2[1] - a1[1])
                k = 0
                while True:
                    point = (a1[0] + offset[0] * k, a1[1] + offset[1] * k)
                    if 0 <= point[0] < max_x and 0 <= point[1] < max_y:
                        antinodes.add(point)
                        k += 1
                    else: break

                k = 0
                while True:
                    point = (a1[0] + offset[0] * k, a1[1] + offset[1] * k)
                    if 0 <= point[0] < max_x and 0 <= point[1] < max_y:
                        antinodes.add(point)
                        k -= 1
                    else: break
    
    return len(antinodes)

if __name__ == "__main__":
    city_map, antennas = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(city_map, antennas))
    print("Solution Star Two:", solution_star_two(city_map, antennas))