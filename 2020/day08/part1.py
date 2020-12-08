accumulator = 0


def execute(instructions):
    global accumulator
    tracker = set()
    i = 0
    while True:
        if i in tracker:
            return
        executedi = i
        op, arg = instructions[i]
        if op == "nop":
            i += 1
        elif op == "acc":
            accumulator += arg
            i += 1
        elif op == "jmp":
            i += arg
        else:
            raise Exception("unknow instruction")
        tracker.add(executedi)


def read_instructions(inputfile):
    instructions = []
    with open(inputfile) as f:
        for line in f:
            op, arg = line.strip().split()
            instructions.append((op, int(arg)))
    return instructions


def main():
    instructions = read_instructions("input")
    execute(instructions)
    print(accumulator)


if __name__ == "__main__":
    main()
