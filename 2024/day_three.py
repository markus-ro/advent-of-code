from pathlib import Path
from sys import argv

import re

SOLUTION_ONE_REGEX = re.compile(r"mul\(\d+\,\d+\)")
SOLUTION_TWO_REGEX = re.compile(r"(mul\(\d+\,\d+\)|do\(\)|don't\(\))")

def solution_star_one(file_content):
    muls = SOLUTION_ONE_REGEX.findall("".join(file_content))
    return sum(int(x[4:]) * int(y[:-1]) for x, y in (mul.split(",") for mul in muls))


def solution_star_two(file_content):
    commands = SOLUTION_TWO_REGEX.findall("".join(file_content))
    do = True
    sum = 0
    for command in commands:
        match command:
            case "do()": do = True
            case "don't()": do = False
            case _:
                if not do: continue
                x, y = command.split(",")
                sum += int(x[4:]) * int(y[:-1])
    
    return sum

if __name__ == "__main__":
    file_content = Path(argv[1]).open().read()
    print("Solution Star One:", solution_star_one(file_content))
    print("Solution Star Two:", solution_star_two(file_content))