from sys import argv
from pathlib import Path
from itertools import combinations
from shapely.geometry import box
from shapely.geometry.polygon import Polygon

def solution_star_one(red_tiles):
    squares = []
    for pair in combinations(red_tiles, 2):
        first_tile, second_tile = pair

        x = abs(first_tile[0] - second_tile[0]) + 1
        y = abs(first_tile[1] - second_tile[1]) + 1

        squares.append((first_tile, second_tile, x*y))
    return sorted(squares, key= lambda x: x[2], reverse=True)

def solution_star_two(red_tiles):
    squares = solution_star_one(red_tiles)
    polygon = Polygon(red_tiles)
    for sq in squares:
        min_x, max_x = min(sq[0][0], sq[1][0]), max(sq[0][0], sq[1][0])
        min_y, max_y = min(sq[0][1], sq[1][1]), max(sq[0][1], sq[1][1])

        if polygon.contains(box(min_x, min_y, max_x, max_y)):
            return sq[2]
        
    return -1    

if __name__ == "__main__":
    red_tiles = [[int(x) for x in line.split(",")] for line in [x.strip() for x in Path(argv[1]).open().readlines()]]
    print("Solution Star One:", solution_star_one(red_tiles)[0][2])
    print("Solution Star Two:", solution_star_two(red_tiles))
