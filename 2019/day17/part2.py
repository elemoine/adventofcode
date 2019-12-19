import itertools
from collections import defaultdict
from collections import deque


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


def findrobot(grid, d={"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}):
    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            if c in ("<", ">", "^", "v"):
                return ((y, x), d[c])


def prefix(s1, s2):
    l = 0
    n = min(len(s1), len(s2))
    for i in range(n):
        if s1[i] != s2[i] or l + len(s1[i]) + 1 > 200:
            return i, s1[:i]
        l += len(s1[i]) + 1
    else:
        return n, s1[:n]


def routinefunctions(s):
    rss = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            l, ss = prefix(s[i:], s[j:])
            if l > 1 and j >= i + l:
                ss = tuple(ss)
                rss[(i, i + l)] = ss
                rss[(j, j + l)] = ss
    keep = []
    for k in sorted(rss.keys()):
        if not keep:
            keep = [k]
            p = k
        elif k[0] == p[1]:
            keep.append(k)
            p = k
    seq = [rss[k] for k in keep]
    print()
    g = itertools.cycle("ABCDEFGHIJKLMNOPQRSTUVWYXZ")
    d = {}
    routine = []
    functions = {}
    for e in seq:
        if e not in d:
            l = next(g)
            d[e] = l
            functions[l] = e
        routine.append(d[e])
    print(routine)
    print(functions)
    # BAD!!
    routine = ['A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'C', 'A']
    functions = {"A": ('R8', 'L4', 'R4', 'R10', 'R8'), "B": ('L12', 'L12', 'R8', 'R8'), "C": ('R10', 'R4', 'R4')}
    # BAD!!
    assert len(functions) == 3
    routine2 = []
    for e in routine:
        routine2.append(ord(e))
        routine2.append(ord(","))
    routine2[-1] = 10
    for f in functions:
        n = []
        for e in functions[f]:
            n.append(ord(e[0]))
            n.append(ord(","))
            for c in e[1:]:
               n.append(ord(c))
            n.append(ord(","))
        n[-1] = 10
        functions[f] = n
    return routine2, functions


def canmove(grid, position, direction):
    assert direction[0] == 0 or direction[1] == 0
    ny = position[0] + direction[0]
    if ny < 0 or ny >= len(grid):
        return False
    nx = position[1] + direction[1]
    if nx < 0 or nx >= len(grid[ny]):
        return False
    return grid[ny][nx] == "#"


def turn(grid, position, direction):
    assert not canmove(grid, position, direction)
    if direction == (-1, 0):
        for k, v in {"L": (0, -1), "R": (0, 1)}.items():
            if canmove(grid, position, v):
                return k, v
    if direction == (1, 0):
        for k, v in {"L": (0, 1), "R": (0, -1)}.items():
            if canmove(grid, position, v):
                return k, v
    if direction == (0, -1):
        for k, v in {"L": (1, 0), "R": (-1, 0)}.items():
            if canmove(grid, position, v):
                return k, v
    if direction == (0, 1):
        for k, v in {"L": (-1, 0), "R": (1, 0)}.items():
            if canmove(grid, position, v):
                return k, v
    return None, None


def move(grid, position, direction):
    position = (position[0] + direction[0], position[1] + direction[1])
    assert grid[position[0]][position[1]] == "#"
    return position


def printmsg(msg):
    if msg:
        print("".join(msg))


def consumeoutput(prog, msg=None):
    if msg is None:
        msg = []
    while True:
        try:
            c = next(prog)
        except StopIteration:
            printmsg(msg)
            raise
        if c is None:
            break
        msg.append(chr(c))
    printmsg(msg)


if __name__ == "__main__":
    with open("input") as f:
        intcode = f.read()

    intcode = intcodetolist(intcode)
    intcode[0] = 2
    prog = program(list(intcode))
    line = []
    grid = []
    while True:
        c = next(prog)
        if c is None:
            break
        if c == 35:
            line.append("#")
        elif c == 46:
            line.append(".")
        elif c == 60:
            line.append("<")
        elif c == 62:
            line.append(">")
        elif c == 118:
            line.append("v")
        elif c == 94:
            line.append("^")
        elif c == 88:
            line.append("X")
        elif c == 10:
            grid.append(line)
            line = []
        else:
            line.append(chr(c))
    displayscaffolds(grid)

    robotpos, robotdir = findrobot(grid)

    n = 0
    path = []
    while True:
        if not canmove(grid, robotpos, robotdir):
            rotation, robotdir = turn(grid, robotpos, robotdir)
            if n:
                path.append(str(n))
            if rotation is None:
                break
            n = 0
            path.append(rotation)
        robotpos = move(grid, robotpos, robotdir)
        n += 1
    path0 = path[::2]
    path1 = path[1::2]
    path = list(e0 + e1 for e0, e1 in zip(path0, path1))
    routine, functions = routinefunctions(path)
  
    msg = []
    for i in routine:
        a = prog.send(i)
        if a:
            msg.append(chr(a))

    for f in ("A", "B", "C"):
        consumeoutput(prog, msg)
        msg = []
        for i in functions[f]:
            a = prog.send(i)
            if a:
                msg.append(chr(a))
    consumeoutput(prog, msg)
    a = prog.send(ord("n"))
    assert a is None
    msg = []
    a = prog.send(10)
    if a:
        msg.append(chr(a))
    while True:
        try:
            c = next(prog)
        except StopIteration:
            printmsg(msg)
            print(c)
            break
        if c:
            msg.append(chr(c))
