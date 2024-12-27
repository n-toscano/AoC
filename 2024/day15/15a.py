datafolder = "data"
with open(f"{datafolder}/15", "r") as file:
    data = file.read()[:-1]

grid = data.split("\n\n")[0].split("\n")
n_rows = len(grid)
n_cols = len(grid[0])
grid = [[grid[x][y] for y in range(n_cols)] for x in range(n_rows)]  # type: ignore
seq = data.split("\n\n")[1].replace("\n", "")


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

        elif grid[x1][y1] == "O":
            while grid[x1][y1] == "O":
                x1, y1 = x1 + dx, y1 + dy

                if grid[x1][y1] == "#":
                    continue
                elif grid[x1][y1] == ".":
                    while (x1, y1) != (x, y):
                        grid[x1][y1] = grid[x1 - dx][y1 - dy]
                        x1, y1 = x1 - dx, y1 - dy
                    x, y = x + dx, y + dy

    return grid


robot_x, robot_y, grid = get_robot(grid)
final_grid = update_grid(grid, robot_x, robot_y, seq)
tot = 0

for x in range(n_rows):
    for y in range(n_cols):
        if final_grid[x][y] == "O":
            tot += 100 * x + y

print(tot)
