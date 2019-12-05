def path(instructions):
    p = set()
    last = (0, 0)
    for i in instructions:
        new = []
        if i[0] == "R":
            for i in range(int(i[1:])):
                new.append((last[0] + (i + 1), last[1]))
        elif i[0] == "L":
            for i in range(int(i[1:])):
                new.append((last[0] - (i + 1), last[1]))
        elif i[0] == "U":
            for i in range(int(i[1:])):
                new.append((last[0], last[1] + (i + 1)))
        elif i[0] == "D":
            for i in range(int(i[1:])):
                new.append((last[0], last[1] - (i + 1)))
        else:
            print("unknown instruction")
            return None
        last = new[-1]
        p |= set(new)
    return p


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def distmin(instructions1, instructions2):
    instructions1 = instructions1.split(",")
    instructions2 = instructions2.split(",")
    p1 = path(instructions1)
    p2 = path(instructions2)
    if p1 is None or p2 is None:
        return None
    dmin = float("+inf")
    for pt in p1 & p2:
       d = dist(pt, centralport)
       if d < dmin:
           dmin = d
    return dmin


if __name__ == "__main__":

    centralport = (0, 0)

    instructions1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    instructions2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert distmin(instructions1, instructions2) == 159

    instructions1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    instructions2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert distmin(instructions1, instructions2) == 135

    with open("input") as f:
        instructions = [l for l in f]
    d = distmin(instructions[0], instructions[1])
    print(d)
