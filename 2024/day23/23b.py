import networkx as nx

datafolder = "data"
with open(f"{datafolder}/23", "r") as file:
    data = file.read()[:-1].split("\n")


connections = set()
for line in data:
    c0, c1 = sorted(line.split("-"))
    if (c0, c1) not in connections:
        connections.add((c0, c1))

LAN = nx.Graph()
LAN.add_edges_from(connections)

cliques = nx.find_cliques(LAN)

max_clique = []  # type: ignore
for clique in cliques:
    if len(clique) > len(max_clique):
        max_clique = clique

print(",".join(sorted(max_clique)))
