datafolder = "data"
with open(f"{datafolder}/01", "r") as file:
    data = file.read()
    lhs, rhs = [], []
    for line in data[:-1].split("\n"):
        lhs.append(int(line[:5]))
        rhs.append(int(line[8:]))

lhs, rhs = sorted(lhs), sorted(rhs)
tot = 0
for left, right in zip(lhs, rhs):
    tot += abs(left - right)
print(tot)
