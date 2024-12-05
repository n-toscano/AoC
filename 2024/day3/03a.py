import re

datafolder = "data"
with open(f"{datafolder}/03", "r") as file:
    data = file.read()


def extract_values(data, pattern):
    matches = re.findall(pattern, data)
    values = [m.strip("mul()").split(",") for m in matches]

    n1s, n2s = zip(*values)
    n1s = list(map(int, n1s))
    n2s = list(map(int, n2s))

    return n1s, n2s


pattern = r"mul\(\d+,\d+\)"

n1s, n2s = extract_values(data, pattern)
products = [n1 * n2 for n1, n2 in zip(n1s, n2s)]

print(sum(products))
