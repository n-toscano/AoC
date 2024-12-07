import numpy as np

datafolder = "data"
with open(f"{datafolder}/06", "r") as file:
    data = file.read()[:-1]


def get_obstacles(data, obst="#"):
    data_array = np.array([list(line) for line in data])
    obstacles = np.vectorize(lambda x: 1 if x in ["#", "0"] else 0)(data_array)
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

        return obstacles

    while inside:
        n_rows, n_cols = obstacles.shape
        obstacles = add_steps_to_obstacle(obstacles)
        if np.any(obstacles > 10000):
            return 1
        guard_pos = rotate_pos(guard_pos, n_cols)
        obstacles = np.rot90(obstacles)

    return 0


def add_object(data, dot_indices, step):
    replace_index = dot_indices[step]
    new_string = data[:replace_index] + "0" + data[replace_index + 1 :]
    return new_string


dot_indices = [i for i, char in enumerate(data) if char == "."]
obs_cnt = 0
for step in range(len(dot_indices)):
    mod_data = add_object(data, dot_indices, step).split("\n")

    obstacles = get_obstacles(mod_data)
    guard_pos = get_guard(mod_data)
    obs_cnt += get_path(guard_pos, obstacles)

print("total steps:", obs_cnt)
