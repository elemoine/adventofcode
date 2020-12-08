from part1 import read_instructions


accumulator = 0


def execute(instructions):
    global accumulator
    _accumulator = accumulator
    tracker = set()
    i = 0
    while i != len(instructions):
        if i in tracker:
            raise Exception("infinite loop")
        j = i
        op, arg = instructions[i]
        if op == "nop":
            i += 1
        elif op == "acc":
            _accumulator += arg
            i += 1
        elif op == "jmp":
            i += arg
        else:
            raise Exception("unknow instruction")
        tracker.add(j)
    accumulator = _accumulator


def change_instruction(instructions, start, switch={"nop": "jmp", "jmp": "nop"}):
    instructions = list(instructions)
    for i in range(start, len(instructions)):
        op, arg = instructions[i]
        if op in switch:
            instructions[i] = (switch[op], arg)
            return instructions, i
    else:
        raise Exception("No instruction to change")


def main():
    instructions = read_instructions("input")
    i = 0
    while True:
        new_instructions, i = change_instruction(instructions, i)
        try:
            execute(new_instructions)
        except Exception as e:
            if str(e) == "infinite loop":
                i += 1
            else:
                raise
        else:
            print(f"Success! accumulator is {accumulator}")
            return


if __name__ == "__main__":
    main()
