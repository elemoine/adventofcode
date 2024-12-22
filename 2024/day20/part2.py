from contextlib import contextmanager

from dijkstra import shortest_distances, shortest_path

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


assert S is not None
assert E is not None

distances, _ = shortest_distances(graph, S)
time_reference = distances[E]
print("Time reference:", time_reference)

path = shortest_path(graph, S, E)
index = {pos: i for i, pos in enumerate(path)}

distances_to_E = {}
for node in path:
    d, _ = shortest_distances(graph, node)
    distances_to_E[node] = d[E]


def manathan_distance(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])


def cheats_from_position(pos):
    cnt = 0
    assert map_[pos[0]][pos[1]] in ("S", "E", ".")
    for y in range(pos[0] - 20, pos[0] + 20 + 1):
        if y < 0 or y > len(map_) - 1:
            continue
        for x in range(pos[1] - 20, pos[1] + 20 + 1):
            if x < 0 or x > len(map_[y]) - 1:
                continue
            if (y, x) == pos:
                continue
            if map_[y][x] not in (".", "E"):
                continue
            assert (y, x) in index
            if index[(y, x)] <= index[pos]:
                continue
            dist = manathan_distance((y, x), pos)
            if dist > 20:
                continue
            assert pos in distances_to_E
            assert (y, x) in distances_to_E
            saved = distances_to_E[pos] - distances_to_E[(y, x)] - dist
            if saved < 100:
                continue
            cnt += 1
    return cnt


cheats = sum(cheats_from_position(pos) for pos in path)
print("Number of cheats:", cheats)
