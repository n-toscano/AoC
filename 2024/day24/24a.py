from collections import deque

datafolder = "data"
with open(f"{datafolder}/24", "r") as file:
    data = file.read()[:-1].split("\n\n")

start_values, ops = data
start_values = start_values.split("\n")  # type: ignore
ops = deque(ops.split("\n"))  # type: ignore
wires = {}
for sv in start_values:
    w, v = sv.split(": ")
    wires[w] = int(v)


def get_output(factors):
    w1, gate, w2 = factors.split(" ")
    if w1 in wires and w2 in wires:
        if gate == "AND":
            return wires[w1] * wires[w2]
        elif gate == "XOR":
            return (wires[w1] + wires[w2]) % 2
        elif gate == "OR":
            return int(wires[w1] + wires[w2] >= 1)
        else:
            raise ("operation non valid")
    return -1


while ops:
    op = ops.popleft()  # type: ignore
    fact, res_wire = op.split(" -> ")
    val = get_output(fact)
    if val >= 0:
        wires[res_wire] = val
    else:
        ops.append(op)  # type: ignore

res = sorted([f"{w}: {v}" for w, v in wires.items() if w[0] == "z"])
tot = "".join([v.split(" ")[1] for v in res[::-1]])
print(int(tot, 2))
