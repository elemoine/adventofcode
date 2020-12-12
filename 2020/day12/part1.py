def ship():
    pos = [0, 0]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dir_ = 2
    while True:
        cmd = yield pos
        action, num = cmd[0], int(cmd[1:])
        if action == "R":
            dir_ = (dir_ + num // 90) % 4
        elif action == "L":
            dir_ = (dir_ + (num * 3) // 90) % 4
        elif action == "F":
            d = directions[dir_]
            pos[0] = pos[0] + num * d[0]
            pos[1] = pos[1] + num * d[1]
        elif action == "W":
            pos[0] -= num
        elif action == "N":
            pos[1] += num
        elif action == "E":
            pos[0] += num
        elif action == "S":
            pos[1] -= num


if __name__ == "__main__":
    with open("input") as f:
        commands = [line.strip() for line in f]
    shipctrl = ship()
    next(shipctrl)
    for cmd in commands:
        pos = shipctrl.send(cmd)
    print(abs(pos[0]) + abs(pos[1]))
