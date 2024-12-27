from collections import deque
from itertools import permutations

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


def get_addend(wire):
    res = sorted([f"{w}: {v}" for w, v in wires.items() if w[0] == wire])
    tot = "".join([v.split(" ")[1] for v in res[::-1]])
    return tot


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


def swap(old_ops, n1, n2, avoid=[]):
    if n1 not in avoid and n2 not in avoid:
        new_ops = old_ops.copy()
        op1 = old_ops[n1]
        op2 = old_ops[n2]

        fact1, res_wire1 = op1.split(" -> ")
        fact2, res_wire2 = op2.split(" -> ")

        new_ops[n1] = fact1 + " -> " + res_wire2
        new_ops[n2] = fact2 + " -> " + res_wire1

        return new_ops
    else:
        return old_ops


x = get_addend("x")
y = get_addend("y")
xy = int(x, 2) + int(y, 2)

old_res = 51657025112326


def swap_couple(ops):
    avoid = []
    for i in range(4):
        cnt = 0
        print(i)
        for n1, n2 in permutations(range(len(ops)), 2):
            print(cnt, end="\r")
            wires = {}
            for sv in start_values:
                w, v = sv.split(": ")
                wires[w] = int(v)
            ops = swap(ops, n1, n2, avoid)
            new_ops = ops.copy()
            c = 0
            while ops and c < 100:
                op = new_ops.popleft()
                fact, res_wire = op.split(" -> ")
                val = get_output(fact)
                if val >= 0:
                    wires[res_wire] = val
                else:
                    new_ops.append(op)
                c += 1

            res = sorted([f"{w}: {v}" for w, v in wires.items() if w[0] == "z"])
            new_res = int("".join([v.split(" ")[1] for v in res[::-1]]), 2)

            cnt += 1

            if abs(new_res - xy) < abs(old_res - xy):
                print(n1, n2)
                avoid.extend([n1, n2])
                ops = new_ops
                break
        print("\n")
    return avoid


print(swap_couple(ops))
