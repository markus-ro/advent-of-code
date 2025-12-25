"""
This file takes as input a file containing a rotation direction alongside a 
distance how far to rotate. The numbers are in the form of a dial with numbers
ranging from 0 to 99.
"""

from sys import argv
from pathlib import Path

def dial(dial_pos, direction, distance):
    is_initial_zero = dial_pos == 0
    extra_zeros, distance = divmod(distance, 100)
    dial_pos += direction * distance

    if dial_pos == 100:
        dial_pos = 0

    if dial_pos > 100:
        extra_zeros += 1
        dial_pos = dial_pos - 100

    if dial_pos < 0:
        extra_zeros += 1 if not is_initial_zero else 0
        dial_pos = 100 + dial_pos
    return dial_pos, extra_zeros

def star_one(lines):
    dial_pos = 50
    password = 0
    for line in lines:
        direction = 1 if line.startswith("R") else -1
        distance = int(line[1:])

        dial_pos, _ = dial(dial_pos, direction, distance)

        if dial_pos == 0: password += 1

    print(password)

def star_two(lines):
    dial_pos = 50
    password = 0
    for line in lines:
        direction = 1 if line.startswith("R") else -1
        distance = int(line[1:].strip())
        dial_pos, extra = dial(dial_pos, direction, distance)

        password += extra
        if dial_pos == 0: password += 1

    print(password)

if __name__ == "__main__":
    lines = Path(argv[1]).open().readlines()
    star_one(lines)
    star_two(lines)