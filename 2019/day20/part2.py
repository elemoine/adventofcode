import sys
import math
import string
from collections import defaultdict


sys.setrecursionlimit(100000)  # Set recursion limit to 10000.


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
    maze[portals["AA"][0][0][0]][portals["AA"][0][0][1]] = "#"
    del portals["AA"]
    end = portals["ZZ"][0][1]
    maze[portals["ZZ"][0][0][0]][portals["ZZ"][0][0][1]] = "#"
    del portals["ZZ"]
    leny = len(maze)
    lenx = len(maze[0])
    portalsinner = {}
    portalsouter = {}
    for k, v in portals.items():
        assert len(v) == 2
        if v[0][0][0] in (1, leny - 2) or v[0][0][1] in (1, lenx - 2):
            portalsouter[v[0][0]] = (v[1][1], k)
            portalsinner[v[1][0]] = (v[0][1], k)
        else:
            portalsinner[v[0][0]] = (v[1][1], k)
            portalsouter[v[1][0]] = (v[0][1], k)
    return start, end, portalsinner, portalsouter


def stepstoexit(start, maze, portalsinner, portalsouter, end, visited, portalsvisited, level, n):
    if start == end and level == 0:
        print("found a path", n)
        return 0
    y, x = start
    if maze[y][x] == "#":
        return -1
    if level == 0 and (y, x) in portalsouter:
        return -1
    if maze[y][x] in string.ascii_uppercase:
        assert (y, x) in portalsinner or (y, x) in portalsouter 
        assert (y, x) in portalsinner or level > 0
        if (y, x, level) in visited:
            print("portal already visited at that level", y, x, level, maze[y][x], level)
            return -1
        visited.add((y, x, level))
        if (y, x) in portalsinner:
            if portalsvisited[(y, x)] > 6:
                print("portal already visited more than 4 times", y, x, maze[y][x], level)
                return -1
            #portalsvisited[(y, x)] += 1
        if (y, x) in portalsinner:
            pos, k = portalsinner[(y, x)]
            level += 1
        else:
            pos, k = portalsouter[(y, x)]
            level -= 1
        y, x = pos
    if (y, x, level) in visited:
        return -1
    visited.add((y, x, level))
    if level > 30:
        return -1
    m = math.inf
    for d in ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)):
        s = stepstoexit(d, maze, portalsinner, portalsouter, end, visited.copy(), portalsvisited.copy(), level, n + 1)
        if s < 0:
            continue
        m = min(m, s + 1)
    if m == math.inf:
        m = -1
    return m


def main(inputfile, expected=None):
    maze = readmaze(inputfile)
    start, end, portalsinner, portalsouter = findportals(maze)
    portalsvisited = defaultdict(int)
    s = stepstoexit(start, maze, portalsinner, portalsouter, end, set(), portalsvisited, 0, 0)
    print(s)
    if expected:
        assert s == expected


if __name__ == "__main__":
    #main("testinput0", 26)
    #main("testinput2")
    main("input")
