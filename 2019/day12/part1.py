import itertools


def pairs(iterable):
    skip = 1
    while True:
        i = iter(iterable)
        s = skip
        while s:
            try:
                v1 = next(i)
            except StopIteration:
                return
            s -= 1
        for v in i:
            yield v1, v
        skip += 1
    

def input(filename):
    with open(filename) as f:
        position = [l.strip() for l in f]
    velocity = []
    for i, _ in enumerate(position):
        pos = position[i][1:-1]
        pos = pos.split(",")
        for j, _ in enumerate(pos):
            coord = int(pos[j].strip()[2:])
            pos[j] = coord
        position[i] = pos
        velocity.append([0, 0, 0])
    return tuple(position), tuple(velocity)


def applygravity(position, velocity):
    indices = range(len(position))
    for i1, i2 in pairs(indices):
        for c in (0, 1, 2):
            if position[i1][c] < position[i2][c]:
                velocity[i1][c] += 1
                velocity[i2][c] -= 1
            elif position[i1][c] > position[i2][c]:
                velocity[i1][c] -= 1
                velocity[i2][c] += 1


def applyvelocity(position, velocity):
    indices = range(len(position))
    for i in indices:
        for c in (0, 1, 2):
            position[i][c] += velocity[i][c]


def energy(position, velocity):
    total = 0
    indices = range(len(position))
    for i in indices:
        pot, kin = 0, 0
        for c in (0, 1, 2):
            pot += abs(position[i][c])
            kin += abs(velocity[i][c])
        total += pot * kin
    return total


def display(position, velocity, energy):
    print()
    for i in range(len(position)):
        print("pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(*position[i], *velocity[i]))
    print("Sum of total energy", energy)


def exec1(inputfile, steps):
    position, velocity = input(inputfile)
    for i in range(0, steps):
        applygravity(position, velocity)
        applyvelocity(position, velocity)
    e = energy(position, velocity)
    display(position, velocity, e)


if __name__ == "__main__":
    exec1("testinput0", 10)
    exec1("testinput1", 100)
    exec1("input", 1000)
