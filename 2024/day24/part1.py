import operator
from collections import deque

OP = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}

wires = {}
gates = deque()

with open("input") as f_:
    section = 0
    for row in f_:
        row = row.strip()
        if ":" in row:
            n, v = row.split(":")
            wires[n] = int(v.strip())
        elif "->" in row:
            left, w3 = row.split("->")
            w1, op, w2 = left.strip().split(" ")
            gates.append((w1.strip(), OP[op.strip()], w2.strip(), w3.strip()))

zwires = {}
while gates:
    w1, op, w2, w3 = gates.popleft()
    if w1 not in wires or w2 not in wires:
        gates.append((w1, op, w2, w3))
    else:
        wires[w3] = op(wires[w1], wires[w2])
        if w3.startswith("z"):
            zwires[w3] = wires[w3]

n = sum(zwires[z] * 2**i for i, z in enumerate(sorted(zwires.keys())))
print(n)
