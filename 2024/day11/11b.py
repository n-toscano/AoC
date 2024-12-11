datafolder = "data"
with open(f"{datafolder}/11", "r") as file:
    data = file.read()[:-1]

cut_dict = {}  # type: ignore
memory_dict = {}  # type:ignore


def cut(n):
    if n in cut_dict:
        return cut_dict[n]

    i = str(n)
    n1 = int(i[: int(len(i) / 2)])
    n2 = int(i[int(len(i) / 2) :])
    cut_dict[i] = (n1, n2)
    return (n1, n2)


def split_count(n, cnt):
    if (n, cnt) in memory_dict:
        return memory_dict[(n, cnt)]
    if cnt == 0:
        out = 1
    elif n == 0:
        out = split_count(1, cnt - 1)
    elif len(str(n)) % 2 == 0:
        n1, n2 = cut(n)
        out = split_count(n1, cnt - 1) + split_count(n2, cnt - 1)
    else:
        out = split_count(n * 2024, cnt - 1)
    memory_dict[(n, cnt)] = out
    return out


numbers = [int(n) for n in data.split(" ")]
tot = 0
for n in numbers:
    tot += split_count(n, 75)
print(tot)
