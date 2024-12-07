import numpy as np

datafolder = "data"
with open(f"{datafolder}/06", "r") as file:
    data = file.read()[:-1].split("\n")


def get_obstacles(data, obst="#"):
    data_array = np.array([list(line) for line in data])
    obstacles = np.vectorize(lambda x: 1 if x == "#" else 0)(data_array)
    return obstacles


def get_guard(data, guard="^"):
    for x, line in enumerate(data):
        y = line.find(guard)
        if y > 0:
            return [x, y]


def rotate_pos(pos, n_cols):
    x, y = pos
    return [n_cols - y - 1, x]


def get_path(guard_pos, obstacles):
    inside = True
    cnt = 2

    def add_steps_to_obstacle(obstacles):
        nonlocal guard_pos, inside, cnt
        col = obstacles[: guard_pos[0], guard_pos[1]]
        y_obs = next((y for y, val in enumerate(col[::-1]) if val == 1), None)
        if y_obs is not None:
            for x in reversed(range(guard_pos[0] - y_obs, guard_pos[0] + 1)):
                obstacles[x, guard_pos[1]] = cnt
                cnt += 1
            guard_pos[0] = guard_pos[0] - y_obs
        else:
            for x in reversed(range(guard_pos[0])):
                obstacles[x, guard_pos[1]] = cnt
                cnt += 1
            inside = False

    while inside:
        n_rows, n_cols = obstacles.shape
        add_steps_to_obstacle(obstacles)
        guard_pos = rotate_pos(guard_pos, n_cols)
        obstacles = np.rot90(obstacles)

    return np.sum(obstacles > 1), obstacles


obstacles = get_obstacles(data)
guard_pos = get_guard(data)
steps, path = get_path(guard_pos, obstacles)

print("total steps:", steps)
