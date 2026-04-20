from collections import defaultdict
from pathlib import Path
from sys import argv

import numpy as np

def parse_lists(file_content: str):
    l1 = np.zeros((len(file_content),), dtype=np.int32)
    l2 = np.zeros((len(file_content),), dtype=np.int32)

    for i, line in enumerate(file_content):
        n1, n2 = line.split("  ")[0], line.split("  ")[1]
        l1[i], l2[i] = int(n1), int(n2)
    
    return l1, l2

def solution_star_one(file_content):
    l1, l2 = parse_lists(file_content)
    l1, l2 = np.sort(l1), np.sort(l2)
    return np.sum(np.abs(l1 - l2))

def solution_star_two(file_content):
    number_count = defaultdict(lambda: 0)
    l1, l2 = parse_lists(file_content)

    for num in l2: number_count[num] += 1

    for i, num in enumerate(l1):
        l1[i] = num * number_count[num]

    return np.sum(l1)

if __name__ == "__main__":
    file_content = Path(argv[1]).open().readlines()
    print("Solution Star One:", solution_star_one(file_content))
    print("Solution Star Two:", solution_star_two(file_content))