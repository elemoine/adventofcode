def initial_state(inputfile):
    state = set()
    with open(inputfile) as f:
        for x, line in enumerate(f):
            line = line.strip()
            for y, value in enumerate(line):
                if value == "#":
                    state.add((x, y, 0))
    return state


def active_cubes(state):
    yield from state


def neighbors(cube):
    x, y, z = cube
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i != 0 or j != 0 or k != 0:
                    yield (x + i, y + j, z + k)


def active_neighbors(cube, state):
    yield from (c for c in neighbors(cube) if c in state)


def count(iter):
    return sum(1 for _ in iter)


def main():
    state = initial_state("input")
    for cycle in range(1, 7):
        newstate = set(state)
        for cube in active_cubes(state):
            if count(active_neighbors(cube, state)) not in (2, 3):
                newstate.remove(cube)
            for neighbor in neighbors(cube):
                if count(active_neighbors(neighbor, state)) == 3:
                    newstate.add(neighbor)
        state = newstate
    print(count(active_cubes(state)))


if __name__ == "__main__":
    main()
