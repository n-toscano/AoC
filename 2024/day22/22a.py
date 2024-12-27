datafolder = "data"
with open(f"{datafolder}/22", "r") as file:
    data = file.read()[:-1].split("\n")


def next(n):
    n1 = ((n * 64) ^ n) % 16777216
    n2 = ((n1 // 32) ^ n1) % 16777216
    n3 = ((n2 * 2048) ^ n2) % 16777216
    return n3


new_ns = []
for n in data:
    for _ in range(2000):
        n = next(int(n))
    new_ns.append(n)

print(sum(new_ns))  # type: ignore
