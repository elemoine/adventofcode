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
        ip_value = execute(instructions[ip_value], ip_value, ip_register, registers)
        ip_value += 1
    return registers


def main():
    ip_register, instructions = read_instructions("input")
    ip_value = 3
    registers = [0, 1, 2, 10551275, 10551275, 0]
    registers = [1, 2, 2, 10551275, 10551275, 0]
    registers = [1, 3, 2, 10551275, 10551275, 0]
    registers = [1, 4, 2, 10551275, 10551275, 0]
    registers = [1, 5, 2, 2110255, 10551275, 0]
    registers = [6, 5, 2, 10551275, 10551275, 0]
    registers = [6, 6, 2, 10551275, 10551275, 0]
    registers = [6, 7, 2, 1507325, 10551275, 0]
    registers = [13, 7, 2, 10551275, 10551275, 0]
    registers = [13, 25, 2, 422051, 10551275, 0]
    registers = [38, 25, 2, 10551275, 10551275, 0]
    registers = [38, 35, 2, 301465, 10551275, 0]
    registers = [73, 35, 2, 10551275, 10551275, 0]
    registers = [73, 175, 2, 60293, 10551275, 0]
    registers = [248, 175, 2, 10551275, 10551275, 0]
    registers = [248, 60293, 2, 175, 10551275, 0]
    registers = [60541, 60293, 2, 10551275, 10551275, 0]
    registers = [60541, 301465, 2, 35, 10551275, 0]
    registers = [362006, 301465, 2, 10551275, 10551275, 0]
    registers = [362006, 422051, 2, 25, 10551275, 0]
    registers = [784057, 422051, 2, 10551275, 10551275, 0]
    registers = [784057, 1507325, 2, 7, 10551275, 0]
    registers = [2291382, 1507325, 2, 10551275, 10551275, 0]
    registers = [2291382, 2110255, 2, 5, 10551275, 0]
    registers = [4401637, 2110255, 2, 10551275, 10551275, 0]
    registers = [4401637, 10551275, 2, 1, 10551275, 0]
    registers = [14952912, 10551275, 2, 10551275, 10551275, 0]
    registers = run(ip_register, ip_value, instructions, registers)
    print(registers[0])


if __name__ == "__main__":
    main()
