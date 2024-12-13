with open("input") as f_:
    rows = [row.strip() for row in f_]


machines = []
machine = None

for row in rows:
    if machine is None:
        machine = {}
    if row == "":
        machines.append(machine)
        machine = None
    elif row.startswith("Button A"):
        xy = row[10:]
        x, y = xy.split(", ")
        x = int(x[2:])
        y = int(y[2:])
        machine["a"] = (x, y)
    elif row.startswith("Button B"):
        xy = row[10:]
        x, y = xy.split(", ")
        x = int(x[2:])
        y = int(y[2:])
        machine["b"] = (x, y)
    elif row.startswith("Prize"):
        xy = row[7:]
        x, y = xy.split(", ")
        x = int(x[2:])
        y = int(y[2:])
        machine["prize"] = (x, y)
machines.append(machine)


print(machines)


total_cost = 0
for idx, machine in enumerate(machines):
    # Px = ax * Ax + bx * Bx
    x = set()
    for ax in range(101):
        tmp = machine["prize"][0] - ax * machine["a"][0]
        if tmp > 0 and tmp % machine["b"][0] == 0:
            bx = tmp // machine["b"][0]
            x.add((ax, bx))

    if not x:
        print(f"[X] No prize {idx}")
        continue

    # Py = ay * Bx + by * By
    y = set()
    for ay in range(101):
        tmp = machine["prize"][1] - ay * machine["a"][1]
        if tmp > 0 and tmp % machine["b"][1] == 0:
            by = (machine["prize"][1] - ay * machine["a"][1]) // machine["b"][1]
            y.add((ay, by))

    if not y:
        print(f"[Y] No prize {idx}")
        continue

    z = x & y
    if not z:
        print(f"[Z] No prize {idx}")
        continue

    print(f"Prize {idx}!!")

    total_cost += min(3 * a + b for a, b in z)

print(total_cost)
