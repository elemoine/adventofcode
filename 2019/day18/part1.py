import math
import string
from collections import defaultdict


def readtunnels(inputfile):
    with open(inputfile) as f:
        tunnels = [[c for c in l.strip()] for l in f]
    return tunnels


def printtunnels(tunnels):
    for l in tunnels:
        for c in l:
            print(c, end="")
        print()


def getstart(tunnels):
    for y in range(len(tunnels)):
        for x in range(len(tunnels[y])):
            if tunnels[y][x] == "@":
                return y, x


def _reachablekeys(y, x, tunnels, keys, visited):
    if tunnels[y][x] == "#":
        return
    if tunnels[y][x] in string.ascii_uppercase and tunnels[y][x].lower() not in keys:
        return
    if (y, x) in visited:
        return
    if "".join(sorted(keys)) == string.ascii_lowercase:
        return
    visited.add((y, x))
    if tunnels[y][x] in string.ascii_lowercase and tunnels[y][x] not in keys:
        key = tunnels[y][x]
        yield y, x, key, 0
        return
    d = defaultdict(list)
    for ky, kx, key, steps in _reachablekeys(y - 1, x, tunnels, keys, visited.copy()):
        d[(ky, kx, key)].append(steps + 1)
    for ky, kx, key, steps in _reachablekeys(y, x + 1, tunnels, keys, visited.copy()):
        d[(ky, kx, key)].append(steps + 1)
    for ky, kx, key, steps in _reachablekeys(y + 1, x, tunnels, keys, visited.copy()):
        d[(ky, kx, key)].append(steps + 1)
    for ky, kx, key, steps in _reachablekeys(y, x - 1, tunnels, keys, visited.copy()):
        d[(ky, kx, key)].append(steps + 1)
    for ky, kx, key in d:
        steps = min(d[(ky, kx, key)])
        yield ky, kx, key, steps


def reachablekeys(y, x, tunnels, keys):
    yield from _reachablekeys(y, x, tunnels, keys, set())


def score(y, x, tunnels, keys, cache={}):
    cachekey = (y, x) + tuple(sorted(keys))
    if cachekey in cache:
        return cache[cachekey]
    r = math.inf
    for ky, kx, key, steps in reachablekeys(y, x, tunnels, keys):
        s = score(ky, kx, tunnels, keys | set([key]), cache) + steps
        r = min(r, s)
    if r == math.inf:
        r = 0
    cache[cachekey] = r
    return r


def main(inputfile, expected=None):
    tunnels = readtunnels(inputfile)
    printtunnels(tunnels)
    y, x = getstart(tunnels)
    s = score(y, x, tunnels, set())
    print("shortest path is {} steps".format(s))
    if expected:
        assert s == expected


if __name__ == "__main__":
    main("testinput0", 86)
    main("testinput1", 132)
    main("testinput2", 136)
    main("testinput3", 81)
    main("input")
