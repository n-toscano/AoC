import re
from itertools import product

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
    p = config(prize, "=")

    min_cost = 0
    for tA, tB in product(range(101), range(101)):
        steps_A = [tA * i for i in A]
        steps_B = [tB * i for i in B]
        steps = tuple([(sa + sb) for sa, sb in zip(steps_A, steps_B)])
        if steps == p:
            print(machine, tA, tB)

            cost = 3 * tA + tB
            if min_cost == 0 or cost < min_cost:
                min_cost = cost

    return min_cost


tot = 0
for machine in data[:10]:
    tot += get_cost(machine)
print(tot)
