from sys import argv
from pathlib import Path
from itertools import combinations
from math import atan2, pi

def solution_star_one(red_tiles, check = None):
    max_space = 0
    for pair in combinations(red_tiles, 2):
        first_tile, second_tile = pair

        if check and not check(first_tile, second_tile): continue

        x = abs(first_tile[0] - second_tile[0]) + 1
        y = abs(first_tile[1] - second_tile[1]) + 1

        max_space = max(max_space, x*y)

    return max_space

def solution_star_two(red_tiles):
    def pip(point):
        # implementation based on https://www.flyriver.com/g/winding-number-algorithm
        winding_num = 0
        px, py = point
        for i in range(len(red_tiles)):
            t1x, t1y = red_tiles[i]
            t2x, t2y = red_tiles[(i + 1) % len(red_tiles)]
            dx1, dy1 = t1x - px, t1y - py
            dx2, dy2 = t2x - px, t2y - py
            delta_angle = atan2(dy2, dx2) - atan2(dy1, dx1)
            delta_angle += -2 * pi if delta_angle > pi else 2 * pi       
            winding_num += delta_angle
        return (winding_num / (2 * pi)) != 0

    def check_square(p1, p2):
        if p1[0] == p2[0] or p1[1] == p2[1]: return True
        return True
    
    return solution_star_one(red_tiles, check_square)

if __name__ == "__main__":
    red_tiles = [[int(x) for x in line.split(",")] for line in [x.strip() for x in Path(argv[1]).open().readlines()]]
    print("Solution Star One: ", solution_star_one(red_tiles))
    print("Solution Star Two: ", solution_star_two(red_tiles))
