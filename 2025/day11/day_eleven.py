import numpy as np

from sys import argv
from pathlib import Path
from functools import reduce

def convert_to_graph(devices):
    mapping = dict()
    devices = [x.replace(":", "").split(" ") for x in devices]
    out_idx, you_idx, idx = -1, -1, 0

    for device in reduce(lambda x,y: x + y, devices):
        if device not in mapping:
            mapping[device] = idx
            idx += 1

        if device == "out": out_idx = mapping[device]
        if device == "you": you_idx = mapping[device]

    graph = np.zeros((idx, idx), dtype=np.uint8)
    for device in devices:
        dev_idx = mapping[device[0]]
        for connection in device[1:]:
            con_idx = mapping[connection]
            graph[dev_idx, con_idx] = 1
    print(mapping)
    return graph, you_idx, out_idx

def dfs(graph):
    pass

def solution_star_one(graph, you_idx, out_idx):
    pass

def solution_star_two(grah, you_idx, out_idx):
    pass

if __name__ == "__main__":
    device_data = [x.strip() for x in Path(argv[1]).open().readlines()]
    #device_data = [x.strip() for x in Path("2025/day11/test_data").open().readlines()]
    graph, you_idx, out_idx = convert_to_graph(device_data)
    print(graph)