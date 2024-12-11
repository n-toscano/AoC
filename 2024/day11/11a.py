datafolder = "data"
with open(f"{datafolder}/11", "r") as file:
    data = file.read()[:-1]


def split(n, cnt=0):
    nn = []
    for i in n:
        if i == "0":
            nn.append("1")
        elif len(i) % 2 == 0:
            nn.append(i[: int(len(i) / 2)])
            nn.append(str(int(i[int(len(i) / 2) :])))
        else:
            nn.append(str(int(i) * 2024))

    cnt += 1
    if cnt < 25:
        return split(nn, cnt)
    else:
        return nn


numbers = data.split(" ")

print(len(split(numbers)))
