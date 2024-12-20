import numpy as np

datafolder = "data"
with open(f"{datafolder}/20", "r") as file:
    data = file.read()[:-1].split("\n")

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def path_length(start, end):
    x, y = start[0], start[1]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    path = np.array([[0, x, y, 1]])
    SEEN = set()
    PATH = []

    while True:
        path = path[path[:, 0].argsort()]
        reward, x, y, dir = path[0]
        path = path[1:]

        if (x, y) == end:
            return int(reward), PATH

        if (x, y, dir) in SEEN:
            continue

        SEEN.add((x, y, dir))
        dx, dy = dirs[dir]
        x1 = x + dx
        y1 = y + dy

        if 0 <= x1 < len(data) and 0 <= y1 < len(data[0]):
            if data[x1][y1] != "#":
                if (x1, y1, dir) not in SEEN:
                    PATH.append((int(x1), int(y1)))
                path = np.vstack((path, [[reward + 1, x1, y1, dir]]))
            path = np.vstack((path, [[reward, x, y, (dir + 1) % 4]]))
            path = np.vstack((path, [[reward, x, y, (dir + 3) % 4]]))


n_rows = len(data)
n_cols = len(data[0])

for i in range(n_rows):
    for j in range(n_cols):
        if data[i][j] == "S":
            start = (i, j)
        elif data[i][j] == "E":
            end = (i, j)

steps = [start]
path, extra_steps = path_length(start, end)
steps.extend(extra_steps)

cnt = 0
for cheat in range(2, 21):
    print(f"{cheat}...", end="\r")
    for i in range(0, len(steps) - 1):
        for j in range(i + 1, len(steps)):
            if distance(steps[i], steps[j]) == cheat:
                new_path = i + (cheat) + (len(steps) - j) - 1
                if path - new_path >= 100:
                    cnt += 1
    print(cheat, cnt)

print(cnt)
