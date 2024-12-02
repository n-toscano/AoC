datafolder = "data"
with open(f"{datafolder}/1.txt", "r") as file:
    data = file.read().split("\n")[:-1]

tot = 0
for s in data:
    i0 = None
    i1 = None
    for i in range(len(s)):
        if s[i].isdigit() and i0 is None:
            i0 = s[i]
        if s[len(s) - i - 1].isdigit() and i1 is None:
            i1 = s[len(s) - i - 1]

    tot += int(i0 + i1)  # type: ignore

print(tot)
