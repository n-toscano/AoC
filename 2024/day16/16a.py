import numpy as np

datafolder = "data"
with open(f"{datafolder}/16", "r") as file:
    data = file.read()[:-1].split("\n")

SEEN = set()


def min_weight_path(start, end):
    x, y = start[0], start[1]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    path = np.array([[0, x, y, 1]])

    while True:
        path = path[path[:, 0].argsort()]
        reward, x, y, dir = path[0]
        path = path[1:]

        if (x, y) == end:
            return reward

        if (x, y, dir) in SEEN:
            continue

        SEEN.add((x, y, dir))
        dx, dy = dirs[dir]
        x1 = x + dx
        y1 = y + dy

        if 0 <= x1 < len(data) and 0 <= y1 < len(data[0]):
            if data[x1][y1] != "#":
                path = np.vstack((path, [[reward + 1, x1, y1, dir]]))
            path = np.vstack((path, [[reward + 1000, x, y, (dir + 1) % 4]]))
            path = np.vstack((path, [[reward + 1000, x, y, (dir + 3) % 4]]))


n_rows = len(data)
n_cols = len(data[0])

for i in range(n_rows):
    for j in range(n_cols):
        if data[i][j] == "S":
            start = (i, j)
        if data[i][j] == "E":
            end = (i, j)

tot = min_weight_path(start, end)
print(tot)
