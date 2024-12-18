import numpy as np

datafolder = "data"
with open(f"{datafolder}/18", "r") as file:
    data = file.read()[:-1].split("\n")


def create_grid(data, lim=1024, n=70):
    bytes = set()
    for line in data[:lim]:
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        bytes.add((y, x))
    grid = "#" * (n + 3) + "\n"
    for i in range(n + 1):
        grid += "#"
        for j in range(n + 1):
            if (i, j) in bytes:
                grid += "#"
            else:
                grid += "."
        grid += "#\n"
    grid += "#" * (n + 3)
    return grid.split("\n")


def shortest_path(start, end):
    y, x = start[0], start[1]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    path = np.array([[0, x, y, 1]])

    while True:
        path = path[path[:, 0].argsort()]
        if len(path) == 0:
            return None
        reward, x, y, dir = path[0]
        path = path[1:]

        if (x, y) == end:
            return int(reward)

        if (x, y, dir) in SEEN:
            continue

        SEEN.add((x, y, dir))
        dx, dy = dirs[dir]
        x1 = x + dx
        y1 = y + dy

        if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
            if grid[x1][y1] != "#":
                path = np.vstack((path, [[reward + 1, x1, y1, dir]]))
            path = np.vstack((path, [[reward, x, y, (dir + 1) % 4]]))
            path = np.vstack((path, [[reward, x, y, (dir + 3) % 4]]))


n = 70
max_b = 0
for b in reversed(range(1024, len(data))):
    SEEN = set()  # type: ignore

    grid = create_grid(data, lim=b, n=n)
    n_rows = len(grid)
    n_cols = len(grid[0])

    start = (1, 1)
    end = (n + 1, n + 1)
    path = shortest_path(start, end)

    if path is None:
        continue
    else:
        print(data[b])
        break
