from sys import argv
from pathlib import Path
from itertools import combinations

NUM_PAIRS = 10

def squared_distance(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return (x1-x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

def find(v, p):
    while p[v] != v:
        p[v] = p[p[v]]
        v = p[v]
    return v

def union(v1, v2, p, s):
    p1, p2 = find(v1, p), find(v2, p)
    if p1 == p2: return 
    if s[p1] < s[p2]: p1, p2 = p2, p1

    p[p2] = p[p1]
    s[p1] += s[p2]

def solution_star_one(verts):
    distances = []
    for pair in combinations(range(len(verts)), 2):
        dis = squared_distance(verts[pair[0]], verts[pair[1]])
        distances.append([dis, pair[0], pair[1]])
    distances = sorted(distances, key=lambda x: x[0])

    parents = list(range(len(verts)))
    sizes = [1] * len(parents)

    for i in range(NUM_PAIRS):
        _, v1, v2 = distances[i]
        union(v1, v2, parents, sizes)
    
    unique_sizes = [sizes[i] for i in range(len(sizes)) if find(i, parents) == i]
    unique_sizes = sorted(unique_sizes, reverse=True)

    fin = 1
    for i in range(3):
        fin *= unique_sizes[i]
    return fin, distances

def solution_star_two(verts, distances):
    parents = list(range(len(verts)))
    sizes = [1] * len(parents)

    for trip in distances:
        union(trip[1], trip[2], parents, sizes)
        if max(sizes) == len(verts):
            return verts[trip[1]][0] * verts[trip[2]][0]



if __name__ == "__main__":
    vert_data = [x.strip() for x in Path(argv[1]).open().readlines()]
    verticies = [[int(x.strip()) for x in row.split(",")] for row in vert_data]

    star_one_product, distances = solution_star_one(verticies)
    print("Solution Star One:", star_one_product)

    print("Solution Star Two:", solution_star_two(verticies, distances))