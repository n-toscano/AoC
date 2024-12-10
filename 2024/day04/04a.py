import re

datafolder = "data"
with open(f"{datafolder}/04", "r") as file:
    data = file.read().split("\n")[:-1]


def find_horizontal(line, pattern):
    matches = re.findall(pattern, line)
    return len(matches)


def find_vertical(data, line_idx, view="top-down"):
    def vshift(idx, view):
        if view == "top-down":
            return idx
        elif view == "bottom-up":
            return -idx

    if view == "top-down" and line_idx > (len(data) - 4):
        return 0
    elif view == "bottom-up" and line_idx < 3:
        return 0

    line = data[line_idx]
    cnt = 0
    match = False
    next_chars = ["M", "A", "S"]
    idx_X = [i for i, c in enumerate(line) if c == "X"]
    for i in idx_X:
        for j, nc in enumerate(next_chars):
            v_shift = vshift((j + 1), view)
            if data[line_idx + v_shift][i] == nc:
                match = True
            else:
                match = False
                break
        if match:
            cnt += 1

    return cnt


def find_diagonal(data, line_idx, view="top-down", orientation="east"):
    def vshift(idx, view):
        if view == "top-down":
            return idx
        elif view == "bottom-up":
            return -idx

    def hshift(idx, shift, view):
        if view == "east":
            return idx + shift
        elif view == "west":
            return idx - shift

    if view == "top-down" and line_idx > (len(data) - 4):
        return 0
    elif view == "bottom-up" and line_idx < 3:
        return 0

    line = data[line_idx]
    cnt = 0
    match = False
    next_chars = ["M", "A", "S"]
    idx_X = [i for i, c in enumerate(line) if c == "X"]

    if orientation == "east":
        idx_X = [i for i in idx_X if i <= (len(line) - 4)]
    elif orientation == "west":
        idx_X = [i for i in idx_X if i >= 3]

    for i in idx_X:
        # print(view, orientation, i)
        for j, nc in enumerate(next_chars):
            v_shift = vshift((j + 1), view)
            h_shift = hshift(i, (j + 1), orientation)
            if data[line_idx + v_shift][h_shift] == nc:
                match = True
            else:
                match = False
                break
        if match:
            cnt += 1

    return cnt


tot = 0
pattern = "XMAS"
for line_idx, line in enumerate(data):
    h_normal = find_horizontal(line, pattern)
    h_reverse = find_horizontal(line, pattern[::-1])

    top_down = find_vertical(data, line_idx, "top-down")
    bottom_up = find_vertical(data, line_idx, "bottom-up")

    diag_SE = find_diagonal(data, line_idx, "top-down", "east")
    diag_NE = find_diagonal(data, line_idx, "bottom-up", "east")
    diag_NW = find_diagonal(data, line_idx, "bottom-up", "west")
    diag_SW = find_diagonal(data, line_idx, "top-down", "west")

    tot += (
        h_normal
        + h_reverse
        + top_down
        + bottom_up
        + diag_SE
        + diag_NE
        + diag_NW
        + diag_SW
    )

print(tot)
