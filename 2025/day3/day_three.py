from sys import argv
from pathlib import Path

def star_one_max_voltage(bank):
    first_idx = 0
    for i in range(1, len(bank) - 1):
        if bank[i] > bank[first_idx]:
            first_idx = i

    second_idx = first_idx + 1
    for i in range(first_idx + 1, len(bank)):
        if bank[i] > bank[second_idx]:
            second_idx = i

    return int(bank[first_idx] + bank[second_idx])

def star_two_max_joltage(bank):
    result = ""
    offset = 11

    idx = -1
    for i in range(12):
        idx += 1
        for j in range(idx, len(bank) - offset  + i):
            if bank[j] > bank[idx]:
                idx = j
        result += bank[idx]

    return int(result)

def get_total_joltage(banks, max_calc):
    total_joltage = 0

    for bank in banks:
        total_joltage += max_calc(bank.strip())

    print(total_joltage)

if __name__ == "__main__":
    banks = Path(argv[1]).open().readlines()
    get_total_joltage(banks, star_one_max_voltage)
    get_total_joltage(banks, star_two_max_joltage)