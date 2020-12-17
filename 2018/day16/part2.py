from collections import defaultdict


def read_input(inputfile):
    with open(inputfile) as f:
        s1, s2 = f.read().split("\n\n\n\n")
    samples = []
    for block in s1.split("\n\n"):
        l1, l2, l3 = block.splitlines()
        registers_b = list(int(c.strip()) for c in l1[9:-1].split(","))
        instruction = tuple(int(c.strip()) for c in l2.split())
        registers_a = list(int(c.strip()) for c in l3[9:-1].split(","))
        samples.append((registers_b, instruction, registers_a))
    instructions = (tuple(int(c) for c in line.split()) for line in s2.splitlines())
    return tuple(samples), tuple(instructions)


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


def sample_opcodes(sample, d):
    for oc in opcodes:
        if execute(oc, sample[1][1:3], sample[1][3], sample[0].copy()) == sample[2]:
            d[oc].add(sample[1][0])


if __name__ == "__main__":
    samples, instructions = read_input("input")
    opcodes_numbers = defaultdict(set)
    for sample in samples:
        sample_opcodes(sample, opcodes_numbers)
    numbers_opcodes = {}
    while opcodes_numbers:
        for oc in opcodes_numbers:
            if len(opcodes_numbers[oc]) == 1:
                r = opcodes_numbers[oc].pop()
                numbers_opcodes[r] = oc
                del opcodes_numbers[oc]
                break
        for oc in opcodes_numbers:
            if len(opcodes_numbers[oc]) > 1:
                opcodes_numbers[oc] -= {r}
    registers = [0, 0, 0, 0]
    for instr in instructions:
        execute(numbers_opcodes[instr[0]], instr[1:3], instr[3], registers)
    print(registers[0])
