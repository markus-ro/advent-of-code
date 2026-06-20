from pathlib import Path
from sys import argv
from itertools import product

def parse_input(file: Path) -> list[list[int]]:
    equations = []
    with file.open() as f:
        for line in f.readlines():
            equations.append(list(map(int, line.strip().replace(":", "").split())))
    return equations

def solution_star_one(equations: list[list[int]]) -> int:
    def is_valid_equation(result: int, numbers: list[int], operators: list[str]) -> bool:
        current_result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == "*":
                current_result *= numbers[i + 1]
            else:
                current_result += numbers[i + 1]

        return result == current_result

    sum_of_possible_values = 0

    for equation in equations:
        for comb in list(product(["+", "*"], repeat=len(equation) - 2)):
            if is_valid_equation(equation[0], equation[1:], comb):
                sum_of_possible_values += equation[0]
                break

    return sum_of_possible_values

def solution_star_two(equations: list[list[int]]) -> int:
    def is_valid_equation(result: int, numbers: list[int], operators: list[str]) -> bool:
        current_result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == "||":
                current_result = int(str(current_result) + str(numbers[i + 1]))
            elif operators[i] == "*":
                current_result *= numbers[i + 1]
            else:
                current_result += numbers[i + 1]

        return result == current_result

    sum_of_possible_values = 0

    for equation in equations:
        for comb in list(product(["+", "*", "||"], repeat=len(equation) - 2)):
            if is_valid_equation(equation[0], equation[1:], comb):
                sum_of_possible_values += equation[0]
                break

    return sum_of_possible_values

if __name__ == "__main__":
    equations = parse_input(Path(argv[1]))
    print("Solution Star One:", solution_star_one(equations))
    print("Solution Star Two:", solution_star_two(equations))