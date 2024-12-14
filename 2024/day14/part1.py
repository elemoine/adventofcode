from collections import Counter

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


def simulate(duration):
    for _ in range(duration):
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


simulate(100)

result = 1
for q in ((0, 0), (1, 0), (0, 1), (1, 1)):
    xmin = q[0] * ((X + 1) // 2)
    xmax = xmin + (X // 2) - 1
    ymin = q[1] * ((Y + 1) // 2)
    ymax = ymin + (Y // 2) - 1
    result *= sum(
        1
        for r in robots
        if r[0][0] >= xmin and r[0][0] <= xmax and r[0][1] >= ymin and r[0][1] <= ymax
    )

print("result:", result)
