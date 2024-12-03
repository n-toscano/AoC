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


def extract_activated(data):
    splits_dont = data.split("don't()")
    do_first = splits_dont[0].replace("do()", "")
    usable_splits_dont = [seq for seq in splits_dont[1:] if "do()" in seq]
    splits_do = [s.split("do()")[1:] for s in usable_splits_dont]
    splits_do = [item for sublist in splits_do for item in sublist]
    splits_do = "".join(splits_do)

    return do_first + splits_do


activated_data = extract_activated(data)
pattern = r"mul\(\d+,\d+\)"

n1s, n2s = extract_values(activated_data, pattern)
products = [n1 * n2 for n1, n2 in zip(n1s, n2s)]

print(sum(products))
