def program(intcode):
    intcode += [0] * 2000
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


def displayscaffolds(lines):
    for l in lines:
        for c in l:
            print(c, end="")
        print()


if __name__ == "__main__":
    with open("input") as f:
        intcode = f.read()
    intcode = intcodetolist(intcode)
    prog = program(intcode)
    line = []
    lines = []
    for c in prog:
        if c == 35:
            line.append("#")
        elif c == 46:
            line.append(".")
        elif c == 10:
            lines.append(line)
            line = []
    lines = lines[:-1]
    displayscaffolds(lines)
    intersections = []
    for y, _ in enumerate(lines):
        if y == 0 or y == len(lines) - 1:
            continue
        for x, _ in enumerate(lines[y]):
            if lines[y][x] != "#" or x == 0 or x == len(lines[y]) - 1:
                continue
            if (lines[y - 1][x] == "#" and lines[y][x + 1] == "#" and
                lines[y + 1][x] == "#" and lines[y][x - 1] == "#"):
                intersections.append((y, x))
    print(sum(y * x for y, x in intersections))
