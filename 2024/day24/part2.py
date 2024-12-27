# Binary Adder
# see https://www.electronics-tutorials.ws/combination/comb_7.html
wires = {}
gates = []

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
            gates.append([w1.strip(), op.strip(), w2.strip(), w3.strip()])


def find_gate(i1, i2, type_):
    return next(
        g
        for g in gates
        if ((g[0] == i1 and g[2] == i2) or (g[0] == i2 and g[2] == i1))
        and g[1] == type_
    )


def find_gate_or_none(i1, i2, type_):
    try:
        return find_gate(i1, i2, type_)
    except StopIteration:
        return None


def find_gate_with_output_wire(wire):
    return next(g for g in gates if g[3] == wire)


x = "x00"
y = "y00"
g = find_gate(x, y, "XOR")
assert g[3] == "z00"
g = find_gate(x, y, "AND")
cout = g[3]

outputs_swapped = []

cin = cout
for i in range(1, 45):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"

    g = find_gate(x, y, "XOR")
    x_xor_y = g[3]

    g = find_gate_or_none(x_xor_y, cin, "XOR")

    if not g:
        # can’t find the XOR gate, so x_xor_y is certainly
        # wrong, so search for the correct one
        gz = find_gate_with_output_wire(z)
        o = gz[2] if gz[0] == cin else gz[0]
        go = find_gate_with_output_wire(o)
        # swap
        x_xor_y, go[3] = go[3], x_xor_y
        outputs_swapped.extend([x_xor_y, go[3]])
        g = find_gate(x_xor_y, cin, "XOR")
    elif g[3] != z:
        # the output of the XOR gate is wrong, so get
        # the gate that has the output we look for and
        # swap
        gz = find_gate_with_output_wire(z)
        # swap
        gz[3], g[3] = g[3], z
        outputs_swapped.extend([g[3], gz[3]])

    g = find_gate(x, y, "AND")
    x_and_y = g[3]

    g = find_gate(x_xor_y, cin, "AND")
    x_xor_y_and_cin = g[3]

    g = find_gate(x_and_y, x_xor_y_and_cin, "OR")
    cout = g[3]

    cin = cout


print(",".join(sorted(outputs_swapped)))
