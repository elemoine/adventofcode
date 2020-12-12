def ship():
    pos = [0, 0]
    wp = [10, 1]
    rotations = {
        0: lambda x, y: (x, y),
        90: lambda x, y: (y, -x),
        180: lambda x, y: (-x, -y),
        270: lambda x, y: (-y, x),
    }
    while True:
        cmd = yield pos
        action, num = cmd[0], int(cmd[1:])
        if action in ("R", "L"):
            if action == "L":
                num = 360 - num
            wp[0], wp[1] = rotations[num](wp[0], wp[1])
        elif action == "F":
            pos[0] += num * wp[0]
            pos[1] += num * wp[1]
        elif action == "W":
            wp[0] -= num
        elif action == "N":
            wp[1] += num
        elif action == "E":
            wp[0] += num
        elif action == "S":
            wp[1] -= num


if __name__ == "__main__":
    with open("input") as f:
        commands = [line.strip() for line in f]
    shipctrl = ship()
    next(shipctrl)
    for cmd in commands:
        pos = shipctrl.send(cmd)
    print(abs(pos[0]) + abs(pos[1]))
