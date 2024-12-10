datafolder = "data"
with open(f"{datafolder}/09", "r") as file:
    data = file.read()[:-1]

memory_idx = [int(d) for i, d in enumerate(data) if i % 2 == 0]
freespace_idx = [int(d) for i, d in enumerate(data) if i % 2 != 0]
disk = [0 for _ in range(memory_idx[0])]

for i in range(1, len(memory_idx)):
    disk += [None for _ in range(freespace_idx[i - 1])]  # type: ignore
    disk += [i for _ in range(memory_idx[i])]

reverse_memory = [i for i in disk if isinstance(i, int)][::-1]

ri = 0
for i in range(len(reverse_memory)):
    if isinstance(disk[i], str):
        disk[i] = reverse_memory[ri]
        ri += 1

disk = disk[: len(reverse_memory)]

print(sum([i * d for i, d in enumerate(disk)]))
