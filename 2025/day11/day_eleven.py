import numpy as np

from sys import argv
from pathlib import Path
from functools import reduce, lru_cache

def convert_to_graph(devices):
    mapping = dict()
    devices = [x.replace(":", "").split(" ") for x in devices]
    idx = 0

    for device in reduce(lambda x,y: x + y, devices):
        if device not in mapping:
            mapping[device] = idx
            idx += 1

    graph = np.zeros((idx, idx), dtype=np.uint8)
    for device in devices:
        dev_idx = mapping[device[0]]
        for connection in device[1:]:
            con_idx = mapping[connection]
            graph[dev_idx, con_idx] = 1
    return graph, mapping

def dfs(graph, node):
    pass

def solution_star_one(graph, map):
    def backtrack(vert):
        acc = 0
        for idx in np.where(graph[vert] == 1)[0]:
            acc += backtrack(idx)
        
        return 1 if vert == map["out"] else acc

    
    return backtrack(map["you"])

def solution_star_two(graph, map):
    @lru_cache(1024)
    def backtrack(vert, dac, fft):
        acc = 0
        if map["dac"] == vert: dac = True
        if map["fft"] == vert: fft = True

        for idx in np.where(graph[vert] == 1)[0]:
            acc += backtrack(idx, dac, fft)

        if vert == map["out"]:
            return 1 if dac and fft else 0
        return acc
    
    res = backtrack(map["svr"], False, False)
    return res

if __name__ == "__main__":
    device_data = [x.strip() for x in Path(argv[1]).open().readlines()]
    device_data_two = [x.strip() for x in Path(argv[2]).open().readlines()]

    graph, mapping = convert_to_graph(device_data)
    print("Solution Star One: ", solution_star_one(graph,mapping))

    graph, mapping = convert_to_graph(device_data_two)
    print("Solution Star Two: ", solution_star_two(graph, mapping))