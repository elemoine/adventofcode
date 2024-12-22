from dijkstra import shortest_distances
from collections import Counter

with open("input") as f_:
    map_ = [list(row.strip()) for row in f_]

graph = {}
S, E = None, None

# get S, E and build graph
for y in range(len(map_)):
    for x in range(len(map_[y])):
        if map_[y][x] == "#":
            continue
        pos = (y, x)
        if map_[y][x] == "S":
            S = pos
        elif map_[y][x] == "E":
            E = pos
        graph[pos] = {}
        for dir_ in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            adj = (y + dir_[0], x + dir_[1])
            if map_[adj[0]][adj[1]] in ("S", "E", "."):
                graph[pos][adj] = 1

times, _ = shortest_distances(graph, S)
time_reference = times[E]

cheats = Counter()

for y in range(1, len(map_) - 1):
    for x in range(1, len(map_[y]) - 1):
        if map_[y][x] != "#":
            continue
        print(f"Remove wall ({y},{x})")
        if map_[y][x - 1] in ("S", "E", ".") and map_[y][x + 1] in ("S", "E", "."):
            graph[(y, x - 1)][(y, x + 1)] = 2
            graph[(y, x + 1)][(y, x - 1)] = 2
            times_, _ = shortest_distances(graph, S)
            del graph[(y, x - 1)][(y, x + 1)]
            del graph[(y, x + 1)][(y, x - 1)]
            cheats[time_reference - times_[E]] += 1
        if map_[y - 1][x] in ("S", "E", ".") and map_[y + 1][x] in ("S", "E", "."):
            graph[(y - 1, x)][(y + 1, x)] = 2
            graph[(y + 1, x)][(y - 1, x)] = 2
            times_, _ = shortest_distances(graph, S)
            del graph[(y - 1, x)][(y + 1, x)]
            del graph[(y + 1, x)][(y - 1, x)]
            cheats[time_reference - times_[E]] += 1

print(cheats)
print(sum(count for saved, count in cheats.items() if saved >= 100))
