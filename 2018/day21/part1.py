def read_instructions(inputfile):
    global ip_reg
    with open(inputfile) as f:
        data = f.read()
    instructions = []
    for line in data.splitlines():
        line = line.strip()
        if line.startswith("#ip "):
            ip_reg = int(line[4:])
        else:
            parts = line.split()
            instructions.append((parts[0], int(parts[1]), int(parts[2]), int(parts[3])))
    return ip_reg, instructions


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


def execute(instruction, ip_value, ip_register, registers):
    opcode, inputs, output = instruction[0], instruction[1:3], instruction[3]
    registers[ip_register] = ip_value
    registers[output] = opcodes[opcode](inputs, registers)
    ip_value = registers[ip_register]
    return ip_value


def run(ip_register, ip_value, instructions, registers):
    while ip_value < len(instructions):
        if ip_value == 28:
            return registers[5]
        ip_value = execute(instructions[ip_value], ip_value, ip_register, registers)
        ip_value += 1


def main():
    ip_register, instructions = read_instructions("input")
    ip_value = 0
    registers = [0, 0, 0, 0, 0, 0]
    result = run(ip_register, ip_value, instructions, registers)
    print(result)


if __name__ == "__main__":
    main()
