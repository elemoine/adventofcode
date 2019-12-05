def program(intcode):
    pos = 0
    while True:
        if pos == len(intcode):
            print("error: reached end of intcode")
            return None
        val = intcode[pos]
        if val == 99:
            return intcode
        if val == 1:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] + intcode[intcode[pos + 2]]
        elif val == 2:
            intcode[intcode[pos + 3]] = intcode[intcode[pos + 1]] * intcode[intcode[pos + 2]]
        else:
            print("error: unknown code")
            return None
        pos += 4


def exec(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    result = program(intcode)
    return result[0] if result else None


if __name__ == "__main__":
    with open("input") as f:
        intcode = [1, 0, 0, 0, 99]
        assert program(intcode) == [2, 0, 0, 0, 99]
        intcode = [2, 3, 0, 3, 99]
        assert program(intcode) == [2, 3, 0, 6, 99]
        intcode = [2, 4, 4, 5, 99, 0]
        assert program(intcode) == [2, 4, 4, 5, 99, 9801]
        intcode = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        assert program(intcode) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

        intcode = f.read().strip()
        intcode = intcode.split(",")
        intcode = list(map(int, intcode))

        result = exec(list(intcode), 12, 2)
        print(result)

        gotit = None
        for noun in range(0, 100):
            goit = None
            for verb in range(0, 100):
                result = exec(list(intcode), noun, verb)
                if result == 19690720:
                    gotit = (noun, verb)
                    break
            if gotit:
                break

        if gotit:
            noun, verb = gotit
            print(100 * noun + verb)
        else:
            print("failed")
