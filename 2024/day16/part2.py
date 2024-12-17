import sys
from collections import defaultdict

with open("input") as f_:
    grid = [list(row.strip()) for row in f_]


def displaygrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
        print()
    print()


def clonegrid(grid):
    c = []
    for y in range(len(grid)):
        r = grid[y].copy()
        c.append(r)
    return c


def shortest_path(pos, dir_):
    score = -1

    d = dir_
    y, x = pos

    stack = [(y, x, d, 0, set())]

    score = sys.maxsize
    visited = {}

    tiles = set()

    while stack:
        y, x, d, v, s = stack.pop()

        k = (y, x, d)
        if k in visited and v > visited[k]:
            continue

        if grid[y][x] == "#":
            continue

        visited[k] = v
        s.add((y, x))

        if grid[y][x] == "E":
            score = min(score, v)
            if v == 89460:
                tiles |= s
            continue

        # pi / 2
        d1 = (d[1], -d[0])
        stack.append((y + d1[0], x + d1[1], d1, v + 1 + 1000, set() | s))

        # -pi / 2
        d2 = (-d[1], d[0])
        stack.append((y + d2[0], x + d2[1], d2, v + 1 + 1000, set() | s))

        # straight
        stack.append((y + d[0], x + d[1], d, v + 1, set() | s))

    return score, len(tiles)


displaygrid(grid)


start = next(
    (y, x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == "S"
)

score, count = shortest_path(start, (0, 1))
print(score, count)
