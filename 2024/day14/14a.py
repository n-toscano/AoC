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


def update_pos(pos, vel, i=0):
    while i < 100:
        new_pos_x = (pos[0] + vel[0]) % n_rows
        new_pos_y = (pos[1] + vel[1]) % n_cols
        new_pos = (new_pos_x, new_pos_y)
        i += 1
        return update_pos(new_pos, vel, i)
    return pos


tl, tr, bl, br = 0, 0, 0, 0
for robot in data:
    p, v = get_pos_vel(robot)
    final_pos = update_pos(p, v)
    if final_pos[0] < (n_rows - 1) / 2 and final_pos[1] < (n_cols - 1) / 2:
        tl += 1
    elif final_pos[0] > (n_rows) / 2 and final_pos[1] < (n_cols - 1) / 2:
        tr += 1
    elif final_pos[0] < (n_rows - 1) / 2 and final_pos[1] > (n_cols) / 2:
        bl += 1
    elif final_pos[0] > (n_rows) / 2 and final_pos[1] > (n_cols) / 2:
        br += 1

print(tl * tr * bl * br)
