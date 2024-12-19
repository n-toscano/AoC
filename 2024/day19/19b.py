datafolder = "data"
with open(f"{datafolder}/19", "r") as file:
    data = file.read()[:-1].split("\n\n")

towels = data[0].replace(" ", "").split(",")
patterns = data[1].split("\n")


def get_matching_towels(pattern):
    mt = set()
    for t in towels:
        if t in pattern:
            mt.add(t)
    return mt


def compile(pattern, towels):
    n = len(pattern)
    out = [0] * (n + 1)
    out[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if pattern[j:i] in towels:
                out[i] += out[j]
    return out[n]


tot = 0
for pattern in patterns:
    mt = get_matching_towels(pattern)
    tot += compile(pattern, mt)


print(tot)
