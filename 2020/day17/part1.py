import itertools


def initial_state(inputfile, dim):
    state = set()
    with open(inputfile) as f:
        for x, line in enumerate(f):
            line = line.strip()
            for y, value in enumerate(line):
                if value == "#":
                    state.add((x, y) + (0,) * (dim - 2))
    return state


def active_cubes(state):
    yield from state


def neighbors(cube, dim):
    yield from (
        tuple(map(sum, zip(cube, d)))
        for d in itertools.product(range(-1, 2), repeat=dim)
        if d != (0,) * dim
    )


def active_neighbors(cube, state, dim):
    yield from (c for c in neighbors(cube, dim) if c in state)


def count(iter):
    return sum(1 for _ in iter)


def main():
    dim = 3
    state = initial_state("input", dim)
    for cycle in range(1, 7):
        newstate = set(state)
        for cube in active_cubes(state):
            if count(active_neighbors(cube, state, dim)) not in (2, 3):
                newstate.remove(cube)
            for neighbor in neighbors(cube, dim):
                if count(active_neighbors(neighbor, state, dim)) == 3:
                    newstate.add(neighbor)
        state = newstate
    print(count(active_cubes(state)))


if __name__ == "__main__":
    main()
