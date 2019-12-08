import itertools


def program(intcode, input):
    pos = 0
    output = []
    while True:
        if pos == len(intcode):
            raise Error("error: reached end of intcode")
        instruction = str(intcode[pos])
        instruction = instruction.rjust(5, "0")
        assert len(instruction) == 5
        opcode = instruction[-2:]
        assert len(opcode) == 2
        if opcode == "99":
            return output
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
            intcode[intcode[pos + 1]] = input.pop()
            pos += 2
        elif opcode == "04":
            # output
            mode1, _, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1)
            output.append(intcode[idx1])
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
    for phases in itertools.permutations(range(5)):
        output = [0]
        for amp in range(5):
            print("running program on amplifier ", amp)
            input = [output[0], phases[amp]]
            output = program(list(intcode), input)
            assert len(output) == 1
        if output[0] > result:
            result = output[0]
    return result


if __name__ == "__main__":
    intcode = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    assert solve(intcode) == 43210
    intcode = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    assert solve(intcode) == 54321
    intcode = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
    assert solve(intcode) == 65210
    with open("input") as f:
        intcode = f.read()
        intcode = intcode.strip()
        print(solve(intcode))
