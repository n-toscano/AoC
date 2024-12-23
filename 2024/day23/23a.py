from itertools import combinations

datafolder = "data"
with open(f"{datafolder}/23", "r") as file:
    data = file.read()[:-1].split("\n")

connections = {}  # type: ignore


def add_connection(line):
    c1, c2 = line.split("-")
    if c1 in connections:
        connections[c1].add(c2)
    else:
        connections[c1] = set([c2])
    if c2 in connections:
        connections[c2].add(c1)
    else:
        connections[c2] = set([c1])

    return connections


def get_tclique(connections):
    cliques = set()
    for c0 in connections:
        c_combs = list(combinations(connections[c0], 2))
        for c1, c2 in c_combs:
            if c1 in connections[c2]:
                clique = (c0, c1, c2)
                if any(c[0] == "t" for c in clique):
                    cliques.add(clique)
    return cliques


for line in data:
    connections = add_connection(line)
print(len(get_tclique(connections)) // 3)
