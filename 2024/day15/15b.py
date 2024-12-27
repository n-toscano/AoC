from collections import deque

datafolder = "data"
with open(f"{datafolder}/15", "r") as file:
    data = file.read()[:-1]


grid = data.split("\n\n")[0].split("\n")
n_rows = len(grid)
n_cols = len(grid[0])
grid = [[grid[x][y] for y in range(n_cols)] for x in range(n_rows)]  # type: ignore
seq = data.split("\n\n")[1].replace("\n", "")
ext_grid = []
for r in range(n_rows):
    row = []
    for c in range(n_cols):
        if grid[r][c] == "#":
            row.append("#")
            row.append("#")
        elif grid[r][c] == "O":
            row.append("[")
            row.append("]")
        elif grid[r][c] == ".":
            row.append(".")
            row.append(".")
        elif grid[r][c] == "@":
            row.append("@")
            row.append(".")
    ext_grid.append(row)

grid = ext_grid  # type: ignore


def get_robot(grid):
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == "@":
                x, y = i, j
                grid[i][j] = "."

    return x, y, grid


def dir(s):
    dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    return dirs[s]


def update_grid(grid, x, y, seq):
    for s in seq:
        dx, dy = dir(s)
        x1, y1 = x + dx, y + dy

        if grid[x1][y1] == "#":
            continue

        elif grid[x1][y1] == ".":
            x, y = x1, y1

        elif grid[x1][y1] in ["[", "]"]:
            go = True
            boxes = deque([(x, y)])
            SEEN = set()

            while boxes:
                x1, y1 = boxes.popleft()
                if (x1, y1) in SEEN:
                    continue
                SEEN.add((x1, y1))
                x2, y2 = x1 + dx, y1 + dy

                if grid[x2][y2] == "#":
                    go = False
                    break
                elif grid[x2][y2] == "[":
                    boxes.append((x2, y2))
                    boxes.append((x2, y2 + 1))
                elif grid[x2][y2] == "]":
                    boxes.append((x2, y2))
                    boxes.append((x2, y2 - 1))
            if not go:
                continue
            while len(SEEN) > 0:
                for x1, y1 in sorted(SEEN):
                    x2, y2 = x1 + dx, y1 + dy
                    if (x2, y2) not in SEEN:
                        grid[x2][y2] = grid[x1][y1]
                        grid[x1][y1] = "."
                        SEEN.remove((x1, y1))
            x, y = x + dx, y + dy

    return grid


robot_x, robot_y, grid = get_robot(grid)
final_grid = update_grid(grid, robot_x, robot_y, seq)
tot = 0

for x in range(n_rows):
    for y in range(n_cols * 2):
        if final_grid[x][y] == "[":
            tot += 100 * x + y

# print("\n".join(["".join([elem for elem in row]) for row in final_grid]))
print(tot)
