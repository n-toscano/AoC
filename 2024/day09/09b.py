datafolder = "data"
with open(f"{datafolder}/09", "r") as f:
    data = f.read()[:-1]

memory_idx = []
freespace_idx = []
memory_val = []
idx = 0
file = 0
disk = []

for i, d in enumerate(data):
    if i % 2 == 0:
        memory_idx.append((idx, int(d)))
        memory_val.append(file)
        for _ in range(int(d)):
            disk.append(file)
            idx += 1
        file += 1
    else:
        freespace_idx.append((idx, int(d)))
        for _ in range(int(d)):
            disk.append(None)  # type: ignore
            idx += 1

for (m_idx, m_legth), memory_val in zip(reversed(memory_idx), reversed(memory_val)):  # type: ignore
    for i, (s_idx, s_length) in enumerate(freespace_idx):
        if s_idx < m_idx and m_legth <= s_length:
            for j in range(m_legth):
                disk[m_idx + j] = None  # type: ignore
                disk[s_idx + j] = memory_val  # type: ignore
            freespace_idx[i] = (s_idx + m_legth, s_length - m_legth)
            break

print(sum([i * d for i, d in enumerate(disk) if d is not None]))
