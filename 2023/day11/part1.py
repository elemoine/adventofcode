import itertools


def distance(galaxy1, galaxy2):
    return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])


def expand(space):
    expanded_y = []
    for y in range(len(space)):
        expanded_y.append(space[y])
        if space[y] == ["."] * len(space[y]):
            expanded_y.append(space[y].copy())

    expanded_y = list(map(list, zip(*expanded_y)))

    expanded = []
    for x in range(len(expanded_y)):
        expanded.append(expanded_y[x])
        if expanded_y[x] == ["."] * len(expanded_y[x]):
            expanded.append(expanded_y[x].copy())

    return list(map(list, zip(*expanded)))


def display(space):
    for y in range(len(space)):
        for x in range(len(space[y])):
            print(space[y][x], end="")
        print()
    print()


if __name__ == "__main__":
    with open("input") as f_:
        space = [list(row.strip()) for row in f_]

    expanded_space = expand(space)

    galaxies = []
    for y in range(len(expanded_space)):
        for x in range(len(expanded_space[y])):
            if expanded_space[y][x] == "#":
                galaxies.append((y, x))

    r = sum(distance(g[0], g[1]) for g in itertools.combinations(galaxies, 2))
    print(r)
