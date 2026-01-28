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

class Machine:
    def __init__(self, target, buttons, joltage):
        self.target, self.size = display_to_int(target)
        self.buttons = [button_to_int(x, self.size) for x in buttons]
        self.joltage = eval(joltage)

def parse_machines(input_file: Path):
    machines = []
    for line in (x.strip() for x in input_file.open().readlines()):
        splitted = line.split(" ")
        machines.append(Machine(splitted[0], splitted[1: -1], splitted[-1]))
    return machines