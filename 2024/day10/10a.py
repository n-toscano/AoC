from collections import deque
from itertools import product

datafolder = "data"
with open(f"{datafolder}/10", "r") as file:
    data = file.read()[:-1].split("\n")


def paths_from_trailhead(head, data):
    x = head[0]
    y = head[1]
    up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
    path = deque([(x, y)])
    summits = set()

    while path:
        x, y = path.popleft()

        if data[x][y] == "9":
            summits.add((x, y))
            continue

        for dx, dy in [up, down, left, right]:
            x1 = x + dx
            y1 = y + dy
            if (
                0 <= x1 < len(data)
                and 0 <= y1 < len(data[0])
                and int(data[x1][y1]) == int(data[x][y]) + 1
            ):
                path.append((x1, y1))

    return len(summits)


n_rows = len(data)
n_cols = len(data[0])

trailheads = [
    (x, y) for x, y in product(range(n_rows), range(n_cols)) if data[x][y] == "0"
]

tot = 0
for head in trailheads:
    tot += paths_from_trailhead(head, data)
print(tot)
