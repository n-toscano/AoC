from itertools import product

datafolder = "data"
with open(f"{datafolder}/04", "r") as file:
    data = file.read().split("\n")[:-1]


def find_mas(data, line_idx, char1="M", char2="M"):
    line = data[line_idx]
    cnt = 0

    middle_char = "A"
    char3 = "S" if char2 == "M" else "M"
    char4 = "S" if char1 == "M" else "M"

    idx_X = [i for i, c in enumerate(line) if c == char1]
    idx_X = [i for i in idx_X if i <= (len(line) - 3)]

    for i in idx_X:
        if (
            line[i + 2] == char2
            and data[line_idx + 1][i + 1] == middle_char
            and data[line_idx + 2][i] == char3
            and data[line_idx + 2][i + 2] == char4
        ):
            cnt += 1

    return cnt


tot = 0
chars = ["M", "S"]
for line_idx in range(len(data) - 2):
    for char1, char2 in product(chars, chars):
        tot += find_mas(data, line_idx, char1, char2)

print(tot)
