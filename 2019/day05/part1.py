def program(intcode):
    pos = 0
    while True:
        if pos == len(intcode):
            print("error: reached end of intcode")
            return None
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
            intcode[intcode[pos + 1]] = int(input())
            pos += 2
        elif opcode == "04":
            # output
            mode1, _, _ = modes(instruction)
            idx1 = modetoindex(mode1, intcode, pos + 1)
            print(intcode[idx1])
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
            print("error: unknown opcode", opcode)
            return None


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


if __name__ == "__main__":
    print("equal 8 test (position mode)")
    intcode = "3,9,8,9,10,9,4,9,99,-1,8"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    print("less than 8 test (position mode)")
    intcode = "3,9,7,9,10,9,4,9,99,-1,8"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    print("equal 8 test (immediate mode)")
    intcode = "3,3,1108,-1,8,3,4,3,99"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    print("less than 8 test (immediate mode)")
    intcode = "3,3,1107,-1,8,3,4,3,99"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    print("jump test (position mode)")
    intcode = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    print("jump test (immediate mode)")
    intcode = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    print("larger example")
    intcode = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    intcode = intcode.split(",")
    intcode = list(map(int, intcode))
    program(intcode)

    with open("input") as f:
        intcode = f.read().strip()
        intcode = intcode.split(",")
        intcode = list(map(int, intcode))
        program(list(intcode))
