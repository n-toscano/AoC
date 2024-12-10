datafolder = "data"
with open(f"{datafolder}/01", "r") as file:
    data = file.read()
    lhs, rhs = [], []
    for line in data[:-1].split("\n"):
        lhs.append(int(line[:5]))
        rhs.append(int(line[8:]))

tot = 0
for left in lhs:
    l_times = 0
    for right in rhs:
        if left == right:
            l_times += 1
    tot += left * l_times
print(tot)
