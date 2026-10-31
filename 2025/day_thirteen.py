import re
from pathlib import Path
from sys import argv

Machine = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]


def parse_machines(input_data: str) -> list[Machine]:
    machines = []
    for block in input_data.strip().split("\n\n"):
        pairs = re.findall(r"[XY][+=]([+-]?\d+)", block)
        if len(pairs) != 6:
            raise ValueError(f"Expected three coordinate pairs in machine: {block!r}")

        values = [int(value) for value in pairs]
        machines.append(
            (
                (values[0], values[1]),
                (values[2], values[3]),
                (values[4], values[5]),
            )
        )
    return machines


def solution_star_one(machines: list[Machine]) -> int:
    total_tokens = 0
    for (ax, ay), (bx, by), (prize_x, prize_y) in machines:
        cheapest = None
        for presses_a in range(101):
            for presses_b in range(101):
                if (
                    presses_a * ax + presses_b * bx == prize_x
                    and presses_a * ay + presses_b * by == prize_y
                ):
                    cost = 3 * presses_a + presses_b
                    if cheapest is None or cost < cheapest:
                        cheapest = cost

        if cheapest is not None:
            total_tokens += cheapest
    return total_tokens


def solution_star_two(machines: list[Machine]) -> int:
    total_tokens = 0
    offset = 10_000_000_000_000
    for (ax, ay), (bx, by), (prize_x, prize_y) in machines:
        prize_x += offset
        prize_y += offset
        determinant = ax * by - ay * bx
        if determinant == 0:
            raise ValueError("Cannot solve a machine with linearly dependent buttons")

        presses_a, remainder_a = divmod(prize_x * by - prize_y * bx, determinant)
        presses_b, remainder_b = divmod(ax * prize_y - ay * prize_x, determinant)
        if remainder_a == 0 and remainder_b == 0 and presses_a >= 0 and presses_b >= 0:
            total_tokens += 3 * presses_a + presses_b
    return total_tokens


if __name__ == "__main__":
    machines = parse_machines(Path(argv[1]).read_text())
    print("Solution Star One:", solution_star_one(machines))
    print("Solution Star Two:", solution_star_two(machines))