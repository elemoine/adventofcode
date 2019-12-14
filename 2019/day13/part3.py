import time
import curses


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
            inp = yield
            intcode[idx1] = inp
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


def movepaddle(move):
    v = 0
    if move[1] > 0:
        v = move[0]
        move[1] -= 1
    return v


def main(stdscr):
    curses.curs_set(False)
    stdscr.clear()
    with open("input") as f:
        intcode = f.read()
    intcode = intcodetolist(intcode)
    intcode[0] = 2  # play for free!
    prog = program(intcode)
    sleeptime = 0.001
    move = [0, 0]
    score = 0
    ball, paddle = None, None
    while True:
        try:
            x = next(prog)
        except StopIteration:
            break
        if x is None:
            x = prog.send(movepaddle(move))
        y = next(prog)
        if y is None:
            y = prog.send(movepaddle(move))
        v = next(prog)
        if v is None:
            v = prog.send(movepaddle(move))
        if x == -1 and y == 0:
            score = v
            continue
        tileid = v
        assert tileid in (0, 1, 2, 3, 4)
        if tileid == 0:
            # empty
            stdscr.addch(y, x, " ")
        if tileid == 1:
            # wall
            stdscr.addch(y, x, "*")
            if y == 23 and x == 41:
                sleeptime = 0.01
        if tileid == 2:
            # block
            stdscr.addch(y, x, "#")
        if tileid == 4:
            # ball
            if ball:
               stdscr.addch(ball[1], ball[0], " ")
            ball = (x, y)
            stdscr.addch(y, x, "0")
        if tileid == 3:
            # paddle
            if paddle:
               stdscr.addch(paddle[1], paddle[0], " ")
            paddle = (x, y)
            stdscr.addch(y, x, "_")
        if tileid in (3, 4) and ball and paddle:
            if ball[0] < paddle[0]:
                move = [-1, paddle[0] - ball[0]]
            elif ball[0] > paddle[0]:
                move = [1, ball[0] - paddle[0]]
            else:
                move = [0, 0]
        stdscr.refresh()
        time.sleep(sleeptime)
    return score


if __name__ == "__main__":
    score = curses.wrapper(main)
    print("final score:", score)
