datafolder = "data"
with open(f"{datafolder}/22", "r") as file:
    data = file.read()[:-1].split("\n")

SEQ = {}  # type: ignore


def next(n):
    n1 = ((n * 64) ^ n) % 16777216
    n2 = ((n1 // 32) ^ n1) % 16777216
    n3 = ((n2 * 2048) ^ n2) % 16777216
    return n3


def check_price(n):
    p = int(str(n)[-1])
    SEQ_INT = []
    s = []
    for _ in range(2000):
        nn = next(n)
        np = int(str(nn)[-1])
        s.append(np - p)
        n = nn
        p = np
        if len(s) == 5:
            s = s[1:]
            st = tuple(s)
            if st in set(SEQ_INT):
                continue
            SEQ_INT.append(st)
            if st in SEQ:
                SEQ[st] += np
                continue
            SEQ[st] = np


for n in data:
    n = int(n)  # type: ignore
    check_price(n)

max_seq = max(SEQ, key=SEQ.get)  # type: ignore
print(SEQ[max_seq])
