def program(intcode):
    intcode += [0] * 1000
    relativebase = 0
    pos = 0
    while True:
        if pos == len(intcode):
            raise Error("error: reached end of intcode")
        instruction = str(intcode[pos])
        instruction = instruction.rjust(5, "0")
        assert len(instruction) == 5
        opcode = instruction[-2:]
        assert len(opcode) == 2
        if opcode == "99":
            return intcode
        if opcode == "01":
            # addition
            mode1, mode2, mode3 = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            idx2 = modetoindex(mode2, intcode, pos + 2, relativebase)
            idx3 = modetoindex(mode3, intcode, pos + 3, relativebase)
            intcode[idx3] = intcode[idx1] + intcode[idx2]
            pos += 4
        elif opcode == "02":
            # multiplication
            mode1, mode2, mode3 = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            idx2 = modetoindex(mode2, intcode, pos + 2, relativebase)
            idx3 = modetoindex(mode3, intcode, pos + 3, relativebase)
            intcode[idx3] = intcode[idx1] * intcode[idx2]
            pos += 4
        elif opcode == "03":
            # input
            mode1, _, _ = modes(instruction)
            assert mode1 in ("0", "2")
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            intcode[idx1] = yield
            pos += 2
        elif opcode == "04":
            # output
            mode1, _, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            yield intcode[idx1]
            pos += 2
        elif opcode == "05":
            # jump-if-true
            mode1, mode2, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            idx2 = modetoindex(mode2, intcode, pos + 2, relativebase)
            if intcode[idx1] != 0:
                pos = intcode[idx2]
            else:
                pos += 3
        elif opcode == "06":
            # jump-if-false
            mode1, mode2, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            idx2 = modetoindex(mode2, intcode, pos + 2, relativebase)
            if intcode[idx1] == 0:
                pos = intcode[idx2]
            else:
                pos += 3
        elif opcode == "07":
            # less than
            mode1, mode2, mode3 = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            idx2 = modetoindex(mode2, intcode, pos + 2, relativebase)
            idx3 = modetoindex(mode3, intcode, pos + 3, relativebase)
            if intcode[idx1] < intcode[idx2]:
                intcode[idx3] = 1
            else:
                intcode[idx3] = 0
            pos += 4
        elif opcode == "08":
            # equals
            mode1, mode2, mode3 = modes(instruction)
            assert mode3 in ("0", "2")
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            idx2 = modetoindex(mode2, intcode, pos + 2, relativebase)
            idx3 = modetoindex(mode3, intcode, pos + 3, relativebase)
            if intcode[idx1] == intcode[idx2]:
                intcode[idx3] = 1
            else:
                intcode[idx3] = 0
            pos += 4
        elif opcode == "09":
            # adjust the relative base
            mode1, _, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1, relativebase)
            relativebase += intcode[idx1]
            pos += 2
        else:
            raise Error("error: unknown opcode", opcode)


def modes(instruction):
    mode1 = instruction[-3:-2]
    assert mode1 in ("0", "1", "2")
    mode2 = instruction[-4:-3]
    assert mode1 in ("0", "1", "2")
    mode3 = instruction[-5:-4]
    assert mode1 in ("0", "1", "2")
    return mode1, mode2, mode3


def modetoindex(mode, intcode, pos, relativebase):
    if mode == "0":
        return intcode[pos]
    elif mode == "1":
        return pos
    elif mode == "2":
        return relativebase + intcode[pos]
    raise Error("error: unknown mode")


def intcodetolist(intcode):
    return list(map(int, intcode.strip().split(",")))


def explore(pos, prog, visited):
    if pos in visited:
        return visited[pos]
    visited[pos] = -1
    distances = []
    for direction in (1, 2, 3, 4):
        status = move(prog, direction)
        if status == 0:
            n = nextpos(pos, direction)
            visited[n] = -1
        elif status == 1:
            n = nextpos(pos, direction)
            d = explore(n, prog, visited)
            if d > 0:
                distances.append(d + 1)
            moveback(prog, direction)
        elif status == 2:
            visited[pos] = 1
            distances.append(1)
            moveback(prog, direction)
            break
    if not distances:
        assert visited[pos] == -1
        return -1
    shorter = min(distances)
    visited[pos] = shorter
    return shorter


def move(prog, direction):
    status = prog.send(direction)
    assert status in (0, 1, 2)
    r = next(prog)
    assert r is None
    return status


def moveback(prog, direction):
    if direction == 1:
        direction = 2
    elif direction == 2:
        direction = 1
    elif direction == 3:
        direction = 4
    elif direction == 4:
        direction = 3
    status = move(prog, direction)
    assert status == 1


def nextpos(pos, direction):
    n = None
    if direction == 1:
        # north
        n = (pos[0], pos[1] + 1)
    elif direction == 2:
        # south
        n = (pos[0], pos[1] - 1)
    elif direction == 3:
        # west
        n = (pos[0] - 1, pos[1])
    elif direction == 4:
        # east
        n = (pos[0] + 1, pos[1])
    assert n is not None
    return n


if __name__ == "__main__":
    with open("input") as f:
        intcode = f.read()
    intcode = intcodetolist(intcode)
    prog = program(intcode)
    r = next(prog)
    assert r is None
    visited = {}
    explore((0, 0), prog, visited)
    print(visited[(0, 0)])
