from sys import argv
from pathlib import Path

def solution_star_one(manifold):
    _m = [list(x) for x in manifold]
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
    _m = [list(x) for x in manifold]
    _paths = [[0 for _ in range(len(_m[0]))] for _ in range(len(_m))]

    for row in range(len(_m)):
        for col in range(len(_m[0])):
            if _m[row][col] == "S":
                _paths[row][col] = 1
            elif _m[row][col] == "^":
                _paths[row + 1][col - 1] += _paths[row - 1][col]
                _paths[row + 1][col + 1] += _paths[row - 1][col]
            else:
                _paths[row][col] += _paths[row - 1][col] if row > 0 else 0
                
    return sum(_paths[-1])

if __name__ == "__main__":
    tachyon_manifold = [x.strip() for x in Path(argv[1]).open().readlines()]

    _splits = solution_star_one(tachyon_manifold)
    print("Solution Star One:", _splits)

    print("Solution Star Two:", solution_star_two(tachyon_manifold))

