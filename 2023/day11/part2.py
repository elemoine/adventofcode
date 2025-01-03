import itertools

with open("input") as f_:
    space = [list(row.strip()) for row in f_]

expand_y = set()
for y in range(len(space)):
    if all(space[y][x] == "." for x in range(len(space[y]))):
        expand_y.add(y)

spacex = list(map(list, zip(*space)))

expand_x = set()
for x in range(len(spacex)):
    if all(spacex[x][y] == "." for y in range(len(spacex[x]))):
        expand_x.add(x)

galaxies = []
for y in range(len(space)):
    for x in range(len(space[y])):
        if space[y][x] == "#":
            galaxies.append((y, x))

N = 1_000_000

r = 0
for g1, g2 in itertools.combinations(galaxies, 2):
    dy = abs(g2[0] - g1[0])
    dy += (N - 1) * len(expand_y & set(range(min(g1[0], g2[0]), max(g1[0], g2[0]))))
    dx = abs(g2[1] - g1[1])
    dx += (N - 1) * len(expand_x & set(range(min(g1[1], g2[1]), max(g1[1], g2[1]))))
    r += dx + dy

print(r)
