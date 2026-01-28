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