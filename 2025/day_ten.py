import pulp as pl

from sys import argv
from pathlib import Path

def display_to_int(display):
    display = display[1:-1]
    int_repr = 0
    for i in range(len(display)):
        int_repr |= 1 << i if display[i] == "#" else 0 << i

    return int_repr, len(display)

def button_to_int(button, display_size):
    button = button[:-1] + ",)"
    buffer = ["."] * display_size
    button_as_tuple = eval(button)
    for n in button_as_tuple:
        buffer[n] = "#"
    return display_to_int("[" + "".join(buffer) + "]")[0]

def button_to_vector(button, dim):
    button = button[:-1] + ",)"
    vec = [0] * dim
    button_as_tuple = eval(button)
    for n in button_as_tuple:
        vec[n] = 1

    return vec

class Machine:
    def __init__(self, target, buttons, joltage):
        self.target, self.size = display_to_int(target)
        self.joltage = eval(joltage.replace("{", "[").replace("}", "]"))
        self.buttons = [button_to_int(x, self.size) for x in buttons]
        self.vectors = [button_to_vector(x, len(self.joltage)) for x in buttons]

def parse_machines(input_file: Path):
    machines = []
    for line in (x.strip() for x in input_file.open().readlines()):
        splitted = line.split(" ")
        machines.append(Machine(splitted[0], splitted[1: -1], splitted[-1]))
    return machines

def solution_star_one(machines):
    fewest_attempts = 0
    for machine in machines:
        states = set([0])
        while machine.target not in states:
            fewest_attempts += 1
            new_states = set()
            for state in states:
                for button in machine.buttons:
                    new_states.add(state ^ button)
            states = new_states

    return fewest_attempts

def solution_star_two(machines):
    minimum_presses = 0
    
    for machine in machines:
        problem = pl.LpProblem("MachineJolt", pl.LpMinimize)
        vars = [pl.LpVariable(f"x{i}", cat="Integer", lowBound=0)
                for i in range(len(machine.vectors))]
        problem += pl.lpSum(vars)

        for i, jolt in enumerate(machine.joltage):
            problem += pl.lpSum(vars[j] * vec[i] for j, vec in enumerate(machine.vectors)) == jolt

        problem.solve(solver=pl.PULP_CBC_CMD(msg=False))
        minimum_presses += int(problem.objective.value())

    return minimum_presses

if __name__ == "__main__":
    machines = parse_machines(Path(argv[1]))

    print("Solution Star One:", solution_star_one(machines))
    print("Solution Star Two:", solution_star_two(machines))