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


if __name__ == "__main__":
    grid = {}
    pos = (0, 0)
    heading = "up"
    usewhite = True
    with open("input") as f:
        intcode = f.read()
    intcode = intcodetolist(intcode)
    prog = program(intcode)
    next(prog)  # start the program
    while True:
        if usewhite:
            assert pos not in grid
            color = 1
            usewhite = False
        else:
            color = grid.get(pos, 0)
        assert color in (0, 1)
        # send the current panel's color to the program, and get the color
        # to paint the current panel with
        color = prog.send(color)
        assert color in (0, 1)
        grid[pos] = color  # paint
        # get the rotation
        rotation = next(prog)
        assert rotation in (0, 1)
        if heading == "up":
            if rotation == 0:
                heading = "left"
                pos = (pos[0] - 1, pos[1])
            else:
                heading = "right"
                pos = (pos[0] + 1, pos[1])
        elif heading == "left":
            if rotation == 0:
                heading = "down"
                pos = (pos[0], pos[1] - 1)
            else:
                heading = "up"
                pos = (pos[0], pos[1] + 1)
        elif heading == "down":
            if rotation == 0:
                heading = "right"
                pos = (pos[0] + 1, pos[1])
            else:
                heading = "left"
                pos = (pos[0] - 1, pos[1])
        elif heading == "right":
            if rotation == 0:
                heading = "up"
                pos = (pos[0], pos[1] + 1)
            else:
                heading = "down"
                pos = (pos[0], pos[1] - 1)
        assert heading in ("up", "left", "down", "right")
        # continue the program
        try:
            next(prog)
        except StopIteration:
            # and we're done!
            break
    newgrid = []
    positions = list(grid.keys())
    xs, ys = zip(*positions)
    for x in range(min(xs), max(xs) + 1):
        line = []
        for y in range(min(ys), max(ys) + 1):
            line.append("*" if grid.get((x, y), 0) == 1 else " ")
        newgrid.append(line)
    for x in range(len(newgrid)):
        for y in range(len(newgrid[x])):
            print(newgrid[x][y], end="")
        print("\n", end="")
