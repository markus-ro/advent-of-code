from sys import argv
from pathlib import Path
from functools import reduce


def parse_input_star_one(puzzle_data):
    ops = puzzle_data[-1].split()
    numbers = [[] for _ in range(len(ops))]
    for line in puzzle_data[:-1]:
        [numbers[i].append(int(x)) for i, x in enumerate(line.split())]

    return numbers, ops

def parse_input_star_two(puzzle_data):
    ops = puzzle_data[-1].split()
    numbers = [[]]
    max_input_width = max([len(x) for x in puzzle_data[:-1]])

    for i in range(max_input_width):
        is_blank_col = True
        num = 0
        for row in puzzle_data[:-1]:
            if i >= len(row): continue
            if not row[i].strip(): continue
            num = num * 10 + int(row[i])
            is_blank_col = False
        
        if is_blank_col:
            numbers.append([])
        else:
            numbers[-1].insert(0, num)

    if not len(numbers[-1]): numbers = numbers[:-1]
    return numbers, ops

def accumulate(numbers, ops):
    result = 0
    for i in range(len(numbers)):
        if ops[i] == "+":
            result += reduce(lambda x, y: x + y, numbers[i])
        else:
            result += reduce(lambda x, y: x * y, numbers[i])
    
    return result

if __name__ == "__main__":
    puzzle_data = Path(argv[1]).open().readlines()

    numbers, ops = parse_input_star_one(puzzle_data)
    print("Solution Star One:", accumulate(numbers, ops))

    numbers, ops = parse_input_star_two(puzzle_data)
    print("Solution Star Two:", accumulate(numbers, ops))
