datafolder = "data"
with open(f"{datafolder}/08", "r") as file:
    data = file.read()[:-1]


def get_resonances(data, resonances=None):
    n_cols = len(data.split("\n")[0])
    data = "".join(data.split("\n"))

    if resonances is None:
        resonances = set()
        dir = "fwd"
    else:
        dir = "bwd"

    for i, c in enumerate(data):
        if c != ".":
            resonants = [j + 1 for j, nc in enumerate(data[i + 1 :]) if nc == c]
            for r in resonants:
                n = 1
                while i + n * r < len(data):
                    if (i + n * r) // n_cols - i // n_cols == n * (
                        (i + r) // n_cols - i // n_cols
                    ):
                        if dir == "fwd":
                            resonances.add(i + n * r)
                        elif dir == "bwd":
                            resonances.add(len(data) - 1 - (i + n * r))
                    n += 1
    return {i for i in resonances if 0 <= i < len(data)}


fwd_resonances = get_resonances(data)

data = data[::-1]
antennas = set([i for i, nc in enumerate(data) if nc != "."])
resonances = get_resonances(data, resonances=fwd_resonances)

print(len(resonances))
