from collections import Counter
from time import sleep

with open("input") as f_:
    rows = [row.strip() for row in f_]

robots = []
for row in rows:
    p, v = row.split(" ")
    p = tuple(map(int, p[2:].split(",")))
    v = tuple(map(int, v[2:].split(",")))
    robots.append([p, v])

X = 101
Y = 103


def tick():
    for r in range(len(robots)):
        robot = robots[r]
        p = robot[0]
        v = robot[1]
        robot[0] = ((p[0] + v[0]) % X, (p[1] + v[1]) % Y)


def display():
    positions = Counter()
    for robot in robots:
        positions[robot[0]] += 1

    for y in range(Y):
        for x in range(X):
            c = "."
            if (x, y) in positions:
                c = str(positions[(x, y)])
            print(c, end="")
        print()


def density(xmin, xmax, ymin, ymax):
    positions = set(robot[0] for robot in robots)
    d = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            d += 1 if (x, y) in positions else 0
    return d


secs = 0

while True:
    tick()
    secs += 1

    densities = []
    for q in ((0, 0), (1, 0), (0, 1), (1, 1)):
        xmin = q[0] * ((X + 1) // 2)
        xmax = xmin + (X // 2) - 1
        ymin = q[1] * ((Y + 1) // 2)
        ymax = ymin + (Y // 2) - 1
        densities.append(density(xmin, xmax, ymin, ymax))

    avg = sum(densities) / 4
    sigma = sum((d - avg) ** 2 for d in densities)
    if sigma > 11000:
        break

display()
print(secs)
