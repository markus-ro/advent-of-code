from sys import argv
from pathlib import Path

def solution_star_one(manifold):
    _m = [list(x) for x in manifold]
    print(_m)
    _splits = 0

    for row in range(1, len(_m)):
        for col in range(len(_m[0])):
            if _m[row - 1][col] == ".":
                continue
            if _m[row][col] == "^" and _m[row - 1][col] == "|":
                _splits += 1
                _m[row][col - 1] = "|"
                _m[row][col + 1] = "|"
            elif _m[row - 1][col] in ["|", "S"]:
                _m[row][col] = "|"

    return _splits

def solution_star_two(manifold):
    _m = [list(x) for x in manifold][:-1]

    for i in range(len(_m[0])): 
        _m[-1][i] = 2 if _m[-1][i] == "^" else 0

    return 0

if __name__ == "__main__":
    tachyon_manifold = [x.strip() for x in Path(argv[1]).open().readlines()]

    print("Star 1:", solution_star_one(tachyon_manifold))

    print("Star 2:", solution_star_two(tachyon_manifold))

