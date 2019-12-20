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


def score(robots, tunnels, keys, cache):
    cachekey = sum(robots, tuple(sorted(keys)))
    if cachekey in cache:
        return cache[cachekey]
    r = math.inf
    for i in range(len(robots)):
        robots_ = robots.copy()
        y, x = robots_[i][0], robots_[i][1]
        for ky, kx, key, steps in reachablekeys(y, x, tunnels, keys):
            robots_[i] = (ky, kx)
            s = score(robots_, tunnels, keys | set([key]), cache) + steps
            r = min(r, s)
    if r == math.inf:
        r = 0
    cache[cachekey] = r
    return r
            

def part2(inputfile, expected=None):
    tunnels = readtunnels(inputfile)
    if inputfile == "input":
        y, x = getstart(tunnels)
        tunnels[y][x] = "#"
        tunnels[y - 1][x] = "#"
        tunnels[y][x - 1] = "#"
        tunnels[y][x + 1] = "#"
        tunnels[y + 1][x] = "#"
        tunnels[y - 1][x - 1] = "@"
        tunnels[y - 1][x + 1] = "@"
        tunnels[y + 1][x - 1] = "@"
        tunnels[y + 1][x + 1] = "@"
    printtunnels(tunnels)
    robots = []
    allkeys = set()
    for y in range(len(tunnels)):
        for x in range(len(tunnels[y])):
            if tunnels[y][x] == "@":
                robots.append((y, x))
            if tunnels[y][x] in string.ascii_lowercase:
                allkeys.add(tunnels[y][x])
    assert len(robots) == 4
    s = score(robots, tunnels, set(), {})
    print("Fewest number of steps to collect all the keys", s)
    if expected:
        assert s == expected


if __name__ == "__main__":
    part2("testinput4", 24)
    part2("testinput5", 32)
    part2("testinput6", 72)
    part2("input")
