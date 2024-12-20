import numpy as np

datafolder = "data"
with open(f"{datafolder}/20", "r") as file:
    data = file.read()[:-1].split("\n")

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid(x, y):
    grade = 0
    ds = []
    for i in range(4):
        if data[x + dirs[i][0]][y + dirs[i][1]] == "#":
            grade += 1
            ds.append(i)
    if grade == 1:
        return True, ds[0]
    elif grade == 2:
        if ds[0] == (ds[1] + 2) % 4:
            return True, ds[0]

    return False, None


def path_length(start, end):
    x, y = start[0], start[1]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    path = np.array([[0, x, y, 1]])
    SEEN = set()

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
            path = np.vstack((path, [[reward, x, y, (dir + 1) % 4]]))
            path = np.vstack((path, [[reward, x, y, (dir + 3) % 4]]))


n_rows = len(data)
n_cols = len(data[0])

for i in range(n_rows):
    for j in range(n_cols):
        if data[i][j] == "S":
            start = (i, j)
        if data[i][j] == "E":
            end = (i, j)

normal_path = path_length(start, end)

cnt = 0
for i in range(1, n_rows - 1):
    for j in range(1, n_cols - 1):
        if data[i][j] == "#":
            val, d = is_valid(i, j)
            if val:
                new_start = (i + dirs[(d + 1) % 4][0], j + dirs[(d + 1) % 4][1])
                new_end = (i + dirs[(d + 3) % 4][0], j + dirs[(d + 3) % 4][1])
                diff = path_length(new_start, new_end) - 2
                if diff >= 100:
                    cnt += 1

print(cnt)
