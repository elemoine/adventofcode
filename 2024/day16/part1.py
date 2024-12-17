import sys

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


# recursive version
# (odes not work)
def _shortest_path(pos, dir_):
    y, x = pos

    if grid[y][x] == "#":
        return -1

    if grid[y][x] == "E":
        return 0

    scores = []

    d = dir_
    r = shortest_path((y + d[0], x + d[1]), d)
    if r >= 0:
        scores.append(r + 1)

    d = (-dir_[1], dir_[0])
    r = shortest_path((y + d[0], x + d[1]), d)
    if r >= 0:
        scores.append(r + 1000 + 1)

    d = (dir_[1], -dir_[0])
    r = shortest_path((y + d[0], x + d[1]), d)
    if r >= 0:
        scores.append(r + 1000 + 1)

    if not scores:
        return -1

    score = min(scores)
    return score


# iterative version
def shortest_path(pos, dir_):
    score = -1

    d = dir_
    y, x = pos

    stack = [(y, x, d, 0)]

    score = sys.maxsize
    visited = {}

    while stack:
        y, x, d, v = stack.pop()

        k = (y, x, d)
        if k in visited and v > visited[k]:
            continue

        if grid[y][x] == "#":
            continue

        visited[k] = v

        if grid[y][x] == "E":
            print(f"Found path to exit! score={v}")
            score = min(score, v)
            continue

        # pi / 2
        d1 = (d[1], -d[0])
        stack.append((y + d1[0], x + d1[1], d1, v + 1 + 1000))

        # -pi / 2
        d2 = (-d[1], d[0])
        stack.append((y + d2[0], x + d2[1], d2, v + 1 + 1000))

        # straight
        stack.append((y + d[0], x + d[1], d, v + 1))

    return score


displaygrid(grid)


start = next(
    (y, x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == "S"
)

score = shortest_path(start, (0, 1))
print(score)
