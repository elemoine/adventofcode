def read_input(inputfile):
    with open(inputfile) as f:
        s1, _ = f.read().split("\n\n\n\n")
    samples = []
    for block in s1.split("\n\n"):
        l1, l2, l3 = block.splitlines()
        registers_b = list(int(c.strip()) for c in l1[9:-1].split(","))
        instruction = tuple(int(c.strip()) for c in l2.split())
        registers_a = list(int(c.strip()) for c in l3[9:-1].split(","))
        samples.append((registers_b, instruction, registers_a))
    return tuple(samples)


opcodes = {
    "addr": lambda i, r: r[i[0]] + r[i[1]],
    "addi": lambda i, r: r[i[0]] + i[1],
    "mulr": lambda i, r: r[i[0]] * r[i[1]],
    "muli": lambda i, r: r[i[0]] * i[1],
    "banr": lambda i, r: r[i[0]] & r[i[1]],
    "bani": lambda i, r: r[i[0]] & i[1],
    "borr": lambda i, r: r[i[0]] | r[i[1]],
    "bori": lambda i, r: r[i[0]] | i[1],
    "setr": lambda i, r: r[i[0]],
    "seti": lambda i, r: i[0],
    "gtir": lambda i, r: 1 if i[0] > r[i[1]] else 0,
    "gtri": lambda i, r: 1 if r[i[0]] > i[1] else 0,
    "gtrr": lambda i, r: 1 if r[i[0]] > r[i[1]] else 0,
    "eqir": lambda i, r: 1 if i[0] == r[i[1]] else 0,
    "eqri": lambda i, r: 1 if r[i[0]] == i[1] else 0,
    "eqrr": lambda i, r: 1 if r[i[0]] == r[i[1]] else 0,
}


def execute(opcode, inputs, output, registers):
    registers[output] = opcodes[opcode](inputs, registers)
    return registers


def behaves_like_three_opcodes(sample):
    return (
        sum(
            int(
                execute(opcode, sample[1][1:3], sample[1][3], sample[0].copy())
                == sample[2]
            )
            for opcode in opcodes
        )
        >= 3
    )


if __name__ == "__main__":
    samples = read_input("input")
    cnt = sum(int(behaves_like_three_opcodes(sample)) for sample in samples)
    print(cnt)
