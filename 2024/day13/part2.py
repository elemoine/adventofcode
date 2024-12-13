import sympy as sy


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
        machine["prize"] = (x + 10000000000000, y + 10000000000000)
machines.append(machine)


total_cost = 0
for idx, machine in enumerate(machines):
    # Px = a * Ax + b * Bx
    # Py = a * Ay + b * By
    Ax = machine["a"][0]
    Bx = machine["b"][0]
    Ay = machine["a"][1]
    By = machine["b"][1]

    Px = machine["prize"][0]
    Py = machine["prize"][1]

    a = sy.Symbol("a")
    b = sy.Symbol("b")

    eq1 = sy.Eq(Ax * a + Bx * b, Px)
    eq2 = sy.Eq(Ay * a + By * b, Py)

    solution = sy.solve((eq1, eq2), (a, b))

    if not isinstance(solution[a], sy.core.numbers.Integer):
        continue

    if not isinstance(solution[b], sy.core.numbers.Integer):
        continue

    total_cost += 3 * int(solution[a]) + int(solution[b])

print(total_cost)
