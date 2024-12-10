datafolder = "data"
with open(f"{datafolder}/08", "r") as file:
    data = file.read()[:-1]


def get_resonances(data):
    n_cols = len(data.split("\n")[0])
    data = "".join(data.split("\n"))
    resonances = set()

    for i, c in enumerate(data):
        if c != ".":
            resonants = [j + 1 for j, nc in enumerate(data[i + 1 :]) if nc == c]
            for r in resonants:
                if (i + 2 * r) // n_cols == 2 * ((i + r) // n_cols) - i // n_cols:
                    resonances.add(i + 2 * r)
                if (i - r) // n_cols == 2 * (i // n_cols) - (i + r) // n_cols:
                    resonances.add(i - r)
    return {i for i in resonances if 0 <= i < len(data)}


resonances = get_resonances(data)

print(len(resonances))
