from sys import argv
from pathlib import Path
from itertools import combinations

def solution_star_one(red_tiles):
    max_space = 0
    for pair in combinations(red_tiles, 2):
        first_tile, second_tile = pair
        x = abs(first_tile[0] - second_tile[0]) + 1
        y = abs(first_tile[1] - second_tile[1]) + 1

        max_space = max(max_space, x*y)

    return max_space

def solution_star_two(red_tiles):
    max_space = 0

if __name__ == "__main__":
    red_tiles = [[int(x) for x in line.split(",")] for line in [x.strip() for x in Path(argv[1]).open().readlines()]]
    print("Solution Star One: ", solution_star_one(red_tiles))
