import numpy as np

datafolder = "data"
with open(f"{datafolder}/16", "r") as file:
    data = file.read()[:-1].split("\n")


def get_path_reward(start, end, way="fwd"):
    SEEN = set()
    x, y = start[0], start[1]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def update_d(d, way):
        return d if way == "fwd" else (d + 2) % 4

    best_path = {}

    if way == "fwd":
        path = np.array([[0, x, y, update_d(1, way)]])
    else:
        path = np.array([[0, x, y, d] for d in range(4)])

    while True:
        path = path[path[:, 0].argsort()]
        reward, x, y, dir = path[0]
        path = path[1:]

        if (x, y, update_d(dir, way)) not in best_path:
            best_path[(x, y, update_d(dir, way))] = reward

        if (x, y) == end:
            return best_path, reward

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

path_fwd, reward = get_path_reward(start, end, "fwd")
path_bwd, _ = get_path_reward(end, start, "bwd")

spots = set()
for i in range(n_rows):
    for j in range(n_cols):
        for d in range(4):
            if (
                (i, j, d) in path_fwd
                and (i, j, d) in path_bwd
                and path_fwd[(i, j, d)] + path_bwd[(i, j, d)] == reward
            ):
                spots.add((i, j))
print(len(spots))
