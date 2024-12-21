registers = []

with open("input") as f_:
    while line := f_.readline().strip():
        _, value = line.split(":")
        registers.append(int(value.strip()))
    _, program = f_.readline().strip().split(":")
    program = list(map(int, program.strip().split(",")))

A, B, C = registers
IP = 0

output = []


def operand_value(operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    assert False


def adv(operand):
    global A, IP
    A = int(A / (2 ** operand_value(operand)))
    IP += 2


def bxl(operand):
    global B, IP
    B = B ^ operand
    IP += 2


def bst(operand):
    global B, IP
    B = operand_value(operand) % 8
    IP += 2


def jnz(operand):
    global IP
    if A != 0:
        IP = operand
    else:
        IP += 2


def bxc(_):
    global B, IP
    B = B ^ C
    IP += 2


def out(operand):
    global IP
    output.append(str(operand_value(operand) % 8))
    IP += 2


def bdv(operand):
    global B, IP
    B = int(A / (2 ** operand_value(operand)))
    IP += 2


def cdv(operand):
    global C, IP
    C = int(A / (2 ** operand_value(operand)))
    IP += 2


instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

while IP < len(program):
    instruction = instructions[program[IP]]
    instruction(program[IP + 1])

print(",".join(output))
