import math
import itertools


def lcm(v1, v2):
    """ Least common multiple.
    """
    return int(v1 * v2 / math.gcd(v1, v2))


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


def findperiod(position, velocity):
    positioninit = tuple(list(p) for p in position)
    velocityinit = tuple(list(v) for v in velocity)
    posxinit, posyinit, poszinit = zip(*positioninit)
    velxinit, velyinit, velzinit = zip(*velocityinit)
    delta, dx, dy, dz = 0, 0, 0, 0
    while True:
        applygravity(position, velocity)
        applyvelocity(position, velocity)
        delta += 1
        posx, posy, posz = zip(*position)
        velx, vely, velz = zip(*velocity)
        if not dx and posx == posxinit and velx == velxinit:
            dx = delta
        if not dy and posy == posyinit and vely == velyinit:
            dy = delta
        if not dz and posz == poszinit and velz == velzinit:
            dz = delta
        if dx and dy and dz:
            break
    return dx, dy, dz


def exec2(inputfile):
    position, velocity = input(inputfile)
    dx, dy, dz = findperiod(position, velocity)
    return lcm(lcm(dx, dy), dz)


if __name__ == "__main__":
    steps = exec2("testinput0")
    assert steps == 2772

    steps = exec2("testinput1")
    assert steps == 4686774924

    steps = exec2("input")
    print("steps:", steps)
