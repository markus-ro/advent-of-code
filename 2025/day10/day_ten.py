import pulp as pl

from sys import argv
from pathlib import Path

from utils import *

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