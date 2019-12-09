import itertools


def program(intcode, amp):
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
            return
        if opcode == "01":
            # addition
            mode1, mode2, mode3 = modes(instruction)
            assert mode3 == "0"
            idx1 = modetoindex(mode1, intcode, pos + 1)
            idx2 = modetoindex(mode2, intcode, pos + 2)
            intcode[intcode[pos + 3]] = intcode[idx1] + intcode[idx2]
            pos += 4
        elif opcode == "02":
            # multiplication
            mode1, mode2, mode3 = modes(instruction)
            assert mode3 == "0"
            idx1 = modetoindex(mode1, intcode, pos + 1)
            idx2 = modetoindex(mode2, intcode, pos + 2)
            intcode[intcode[pos + 3]] = intcode[idx1] * intcode[idx2]
            pos += 4
        elif opcode == "03":
            # input
            mode1, _, _ = modes(instruction)
            assert mode1 == "0"
            intcode[intcode[pos + 1]] = yield
            pos += 2
        elif opcode == "04":
            # output
            mode1, _, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1)
            yield intcode[idx1]
            pos += 2
        elif opcode == "05":
            # jump-if-true
            mode1, mode2, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1)
            idx2 = modetoindex(mode2, intcode, pos + 2)
            if intcode[idx1] != 0:
                pos = intcode[idx2]
            else:
                pos += 3
        elif opcode == "06":
            # jump-if-false
            mode1, mode2, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1)
            idx2 = modetoindex(mode2, intcode, pos + 2)
            if intcode[idx1] == 0:
                pos = intcode[idx2]
            else:
                pos += 3
        elif opcode == "07":
            # less than
            mode1, mode2, mode3 = modes(instruction)
            assert mode3 == "0"
            idx1 = modetoindex(mode1, intcode, pos + 1)
            idx2 = modetoindex(mode2, intcode, pos + 2)
            if intcode[idx1] < intcode[idx2]:
                intcode[intcode[pos + 3]] = 1
            else:
                intcode[intcode[pos + 3]] = 0
            pos += 4
        elif opcode == "08":
            # equals
            mode1, mode2, mode3 = modes(instruction)
            assert mode3 == "0"
            idx1 = modetoindex(mode1, intcode, pos + 1)
            idx2 = modetoindex(mode2, intcode, pos + 2)
            if intcode[idx1] == intcode[idx2]:
                intcode[intcode[pos + 3]] = 1
            else:
                intcode[intcode[pos + 3]] = 0
            pos += 4
        else:
            raise Error("error: unknown opcode {}".format(opcode))
    raise Error("error: normally unreachable code section reached")


def modes(instruction):
    mode1 = instruction[-3:-2]
    assert mode1 in ("0", "1")
    mode2 = instruction[-4:-3]
    assert mode2 in ("0", "1")
    mode3 = instruction[-5:-4]
    assert mode3 in ("0", "1")
    return mode1, mode2, mode3


def modetoindex(mode, intcode, pos):
    return intcode[pos] if mode == "0" else pos


def solve(intcode):
    intcode = list(map(int, intcode.split(",")))
    result = float("-inf")
    for phases in itertools.permutations(range(5, 10)):
        assert len(phases) == 5
        programs = []
        for amp in range(5):
            prog = program(list(intcode), amp)
            next(prog)  # start the program
            prog.send(phases[amp])  # send phase to program
            programs.append((amp, prog))
        input = 0
        for amp, prog in itertools.cycle(programs):
            output = prog.send(input)  # send signal to program, and get output
            try:
                next(prog)  # continue program
            except StopIteration:
                if amp == 4:
                    break  # wait for amplifier E to halt
            input = output
        result = max(output, result)
    return result


if __name__ == "__main__":
    intcode = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    result = solve(intcode)
    assert result == 139629729
    intcode = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    result = solve(intcode)
    assert result == 18216
    with open("input") as f:
        intcode = f.read()
        intcode = intcode.strip()
        result = solve(intcode)
        print(result)
        assert result == 17279674
