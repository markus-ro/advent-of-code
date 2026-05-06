from pathlib import Path
from sys import argv

import numpy as np

def parse_file_content(file_content):
    for line in file_content:
        yield np.array([int(x) for x in line.split(" ")])

def solution_star_one(file_content):
    def is_safe(in_list: np.array):
        diffs = np.diff(in_list)
        if np.any(diffs == 0): return False
        if np.any(diffs > 0) and np.any(diffs < 0): return False
        if np.any(np.abs(diffs) > 3): return False
        return True

    valid = 0
    for list in parse_file_content(file_content):
        valid += 1 if is_safe(list) else 0
    
    return valid

def solution_star_two(file_content):
    def is_safe(diffs: np.array):
        if np.any(diffs == 0): return False
        if np.any(diffs > 0) and np.any(diffs < 0): return False
        if np.any(np.abs(diffs) > 3): return False
        return True
    
    def check_list(in_list: np.array):
        diffs = np.diff(in_list)
        if is_safe(diffs): return True
        
        # Check if removing any element might make it safe
        for i in range(len(in_list)):
            new_list = np.delete(in_list, i)
            if is_safe(np.diff(new_list)):
                return True
            
        return False

    valid = 0
    for list in parse_file_content(file_content):
        valid += 1 if check_list(list) else 0

    return valid
        


if __name__ == "__main__":
    file_content = Path(argv[1]).open().readlines()
    print("Solution Star One:", solution_star_one(file_content))
    print("Solution Star Two:", solution_star_two(file_content))