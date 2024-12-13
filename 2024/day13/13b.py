import re
from itertools import product

import numpy as np

datafolder = "data"
with open(f"{datafolder}/13", "r") as file:
    data = file.read()[:-1].split("\n\n")


def config(line, op):
    line = line.split(":")[1]

    match_x = re.search(rf"X\{op}(\d+)", line)
    match_y = re.search(rf"Y\{op}(\d+)", line)

    X = int(match_x.group(1))
    Y = int(match_y.group(1))

    return X, Y


def get_cost(machine):
    buttonA, buttonB, prize = machine.split("\n")
    A = config(buttonA, "+")
    B = config(buttonB, "+")
    p = tuple([c + 10000000000000 for c in config(prize, "=")])

    a = [[A[0], B[0]], [A[1], B[1]]]
    x = np.linalg.solve(a, p)
    for tA, tB in product(
        [int(np.floor(x[0])), int(np.ceil(x[0]))],
        [int(np.floor(x[1])), int(np.ceil(x[1]))],
    ):
        if tA * A[0] + tB * B[0] == p[0] and tA * A[1] + tB * B[1] == p[1]:
            return 3 * tA + tB

    return 0


tot = 0
for machine in data:
    tot += get_cost(machine)
print(tot)
