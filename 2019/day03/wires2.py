def path(instructions):
    s = 0
    p = {}
    last = (0, 0)
    for instruction in instructions:
        if instruction[0] == "R":
            for i in range(1, int(instruction[1:]) + 1):
                s += 1
                key = (last[0] + i, last[1])
                if key not in p:
                    p[key] = s
            last = (last[0] + int(instruction[1:]), last[1])
        elif instruction[0] == "L":
            for i in range(1, int(instruction[1:]) + 1):
                s += 1
                key = (last[0] - i, last[1])
                if key not in p:
                    p[key] = s
            last = (last[0] - int(instruction[1:]), last[1])
        elif instruction[0] == "U":
            for i in range(1, int(instruction[1:]) + 1):
                s += 1
                key = (last[0], last[1] + i)
                if key not in p:
                    p[key] = s
            last = (last[0], last[1] + int(instruction[1:]))
        elif instruction[0] == "D":
            for i in range(1, int(instruction[1:]) + 1):
                s += 1
                key = (last[0], last[1] - i)
                if key not in p:
                    p[key] = s
            last = (last[0], last[1] - int(instruction[1:]))
        else:
            print("unknown instruction")
            return None
    return p


def stepmin(instructions1, instructions2):
    instructions1 = instructions1.split(",")
    instructions2 = instructions2.split(",")
    p1 = path(instructions1)
    p2 = path(instructions2)
    if p1 is None or p2 is None:
        return None
    intersections = set(p1.keys()) & set(p2.keys())
    smin = float("+inf")
    for intersection in intersections:
        s = p1[intersection] + p2[intersection]
        if s < smin:
            smin = s
    return smin

if __name__ == "__main__":

    instructions1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    instructions2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    s = stepmin(instructions1, instructions2)
    assert s == 610

    instructions1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    instructions2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    s = stepmin(instructions1, instructions2)
    assert s == 410

    with open("input") as f:
        instructions = [l for l in f]
    s = stepmin(instructions[0], instructions[1])
    print(s)
