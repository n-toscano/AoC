from collections import deque

datafolder = "data"
with open(f"{datafolder}/12", "r") as file:
    data = file.read()[:-1].split("\n")

n_rows = len(data)
n_cols = len(data[0])
SEEN = set()
up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)


def count_consecutive_groups(arr):
    groups = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            groups += 1

    return groups


def get_garden(spot):
    garden_cnt = deque([spot])
    garden = set([spot])
    perimeter = {}

    while garden_cnt:
        garden.update(set(garden_cnt))
        x, y = garden_cnt.popleft()
        if (x, y) in SEEN:
            continue
        SEEN.add((x, y))
        for dx, dy in [up, down, left, right]:
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 < n_rows and 0 <= y1 < n_cols and data[x1][y1] == data[x][y]:
                garden_cnt.append((x1, y1))
            else:
                if (dx, dy) not in perimeter:
                    perimeter[(dx, dy)] = set()
                perimeter[(dx, dy)].add((x, y))

    area = len(garden)
    sides = 0

    for k, v in perimeter.items():
        if k[1] in [1, -1]:
            ys = set(p[1] for p in v)
            for y in ys:
                xs = sorted([p[0] for p in v if p[1] == y])
                sides += count_consecutive_groups(xs)

        if k[0] in [1, -1]:
            xs = set(p[0] for p in v)
            for x in xs:
                ys = sorted(list(p[1] for p in v if p[0] == x))
                sides += count_consecutive_groups(ys)

    return area * sides


tot = 0
for r in range(n_rows):
    for c in range(n_cols):
        if (r, c) not in SEEN:
            tot += get_garden((r, c))
print(tot)
