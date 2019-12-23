import sys
import math
import string
from collections import defaultdict


sys.setrecursionlimit(10000)  # Set recursion limit to 10000.


def readmaze(inputfile):
    maze = []
    with open(inputfile) as f:
        for l in f:
            line = l.rstrip("\n")
            maze.append(list(line))
    for l in maze:
        for c in l:
            print(c, end="")
        print()
    return maze


def findportals(maze):
    portals = defaultdict(list)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] in string.ascii_uppercase:
                if y < len(maze) - 1 and maze[y + 1][x] in string.ascii_uppercase:
                    key = maze[y][x] + maze[y + 1][x]
                    if y < len(maze) - 2 and maze[y + 2][x] == ".":
                        portals[key].append(((y + 1, x), (y + 2, x)))
                    else:
                        assert y > 0 and maze[y - 1][x] == "."
                        portals[key].append(((y, x), (y - 1, x)))
                elif x < len(maze[y]) - 1 and maze[y][x + 1] in string.ascii_uppercase:
                    key = maze[y][x] + maze[y][x + 1]
                    if x < len(maze[y]) - 2 and maze[y][x + 2] == ".":
                        portals[key].append(((y, x + 1), (y, x + 2)))
                    else:
                        assert x > 0 and maze[y][x - 1] == "."
                        portals[key].append(((y, x), (y, x - 1)))
    start = portals["AA"][0][1]
    maze[portals["AA"][0][0][0]][portals["AA"][0][0][1]] = "#"  # close the entrance
    del portals["AA"]
    end = portals["ZZ"][0][1]
    del portals["ZZ"]
    portalsfinal = {}
    for k, v in portals.items():
        assert len(v) == 2
        portalsfinal[v[0][0]] = (v[1][1], k)
        portalsfinal[v[1][0]] = (v[0][1], k)
    return start, end, portalsfinal


def stepstoexit(start, maze, portals, end, visited, n):
    if start == end:
        return 0
    y, x = start
    if maze[y][x] == "#":
        return -1
    if (y, x) in visited:
        return -1
    visited.add((y, x))
    if maze[y][x] in string.ascii_uppercase:
        assert (y, x) in portals
        pos, k = portals[(y, x)]
        y, x = pos
        visited.add((y, x))
    m = math.inf
    for d in ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)):
        s = stepstoexit(d, maze, portals, end, visited.copy(), n + 1)
        if s < 0:
            continue
        m = min(m, s + 1)
    if m == math.inf:
        m = -1
    return m


def main(inputfile, expected=None):
    maze = readmaze(inputfile)
    start, end, portals = findportals(maze)
    s = stepstoexit(start, maze, portals, end, set(), 0)
    print(s)
    if expected:
        assert s == expected


if __name__ == "__main__":
    main("testinput0", 23)
    main("testinput1", 58)
    main("input")
