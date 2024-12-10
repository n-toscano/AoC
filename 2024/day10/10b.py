from itertools import product

datafolder = "data"
with open(f"{datafolder}/10", "r") as file:
    data = file.read()[:-1].split("\n")


def total_paths(head, data):
    x, y = head[0], head[1]
    up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)

    if data[x][y] == "9":
        return 1

    tot = 0
    for dx, dy in [up, down, left, right]:
        x1 = x + dx
        y1 = y + dy
        if (
            0 <= x1 < len(data)
            and 0 <= y1 < len(data[0])
            and int(data[x1][y1]) == int(data[x][y]) + 1
        ):
            tot += total_paths((x1, y1), data)

    return tot


n_rows = len(data)
n_cols = len(data[0])

trailheads = [
    (x, y) for x, y in product(range(n_rows), range(n_cols)) if data[x][y] == "0"
]

tot = 0
for head in trailheads:
    tot += total_paths(head, data)
print(tot)
