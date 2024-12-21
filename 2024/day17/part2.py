import itertools
from time import sleep

registers = []

with open("input") as f_:
    while line := f_.readline().strip():
        _, value = line.split(":")
        registers.append(int(value.strip()))
    _, program = f_.readline().strip().split(":")
    program = list(map(int, program.strip().split(",")))

_, B, C = registers


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
    output.append(operand_value(operand) % 8)
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

print("program:", program)

# A = 2 ** 45 for 16 figures in the output

# every 2^9 output[3] changes
# every 2^12 output[4] changes
# every 2^15 output[5] changes
# every 2^18 output[6] changes
# every 2^21 output[7] changes
# every 2^24 output[8] changes
# every 2^27 output[9] changes
# every 2^30 output[10] changes
# every 2^33 output[11] changes
# every 2^36 output[12] changes
# every 2^39 output[13] changes
# every 2^42 output[14] changes
# every 2^45 output[15] changes

a, inc, power = 0, 0, 45
track = []

while True:
    a += inc

    A = a
    IP = 0
    output = []

    while IP < len(program):
        instruction = instructions[program[IP]]
        instruction(program[IP + 1])

    if output == program:
        print("Got it!")
        break

    if len(output) > len(program):
        # back track
        a, power = track.pop()
        i = 1
        continue

    assert power % 3 == 0

    idx = power // 3
    if output[idx:] == program[idx:]:
        track.append((a, power))
        power -= 3
        inc = 0
    else:
        inc = 2**power

print("A:", a)
