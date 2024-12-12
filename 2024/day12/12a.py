from collections import deque

datafolder = "data"
with open(f"{datafolder}/12", "r") as file:
    data = file.read()[:-1].split("\n")

n_rows = len(data)
n_cols = len(data[0])
SEEN = set()
up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)


def get_garden(spot):
    garden = deque([spot])
    area = 0
    perimeter = 0

    while garden:
        x, y = garden.popleft()
        if (x, y) in SEEN:
            continue
        SEEN.add((x, y))
        area += 1
        for dx, dy in [up, down, left, right]:
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 < n_rows and 0 <= y1 < n_cols and data[x1][y1] == data[x][y]:
                garden.append((x1, y1))
            else:
                perimeter += 1

    return area * perimeter


tot = 0
for r in range(n_rows):
    for c in range(n_cols):
        if (r, c) not in SEEN:
            tot += get_garden((r, c))
print(tot)
