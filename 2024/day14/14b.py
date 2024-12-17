import re

datafolder = "data"
with open(f"{datafolder}/14", "r") as file:
    data = file.read()[:-1].split("\n")

n_rows = 101
n_cols = 103


def get_pos_vel(robot):
    pattern = r"p=(\d+,\d+)\s+v=(-?\d+,-?\d+)"
    match = re.search(pattern, robot)
    p_tuple = tuple(map(int, match.group(1).split(",")))
    v_tuple = tuple(map(int, match.group(2).split(",")))
    return p_tuple, v_tuple


def update_pos(pos, vel):
    new_pos_x = (pos[0] + vel[0]) % n_rows
    new_pos_y = (pos[1] + vel[1]) % n_cols
    return (new_pos_x, new_pos_y)


tree = False
cnt = 0

positions = n_cols * n_rows * [(0, 0)]

while not tree:
    tiles_list = []
    for i, robot in enumerate(data):
        if cnt == 0:
            p, v = get_pos_vel(robot)
        else:
            p = positions[i]
            _, v = get_pos_vel(robot)
        new_pos = update_pos(p, v)
        positions[i] = new_pos
        tiles_list.append(new_pos)

    cnt += 1
    tiles = set(tiles_list)
    tree = True if len(tiles) == len(tiles_list) else False
    print(cnt, end="\r")

print(cnt)
