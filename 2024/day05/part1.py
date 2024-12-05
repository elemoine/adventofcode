from collections import defaultdict

f_ = open("input")

deps = defaultdict(set)
updates = []

read_deps = True

for line in f_:
    line = line.strip()
    if line == "":
        read_deps = False
        continue
    if read_deps:
        # a must be printed before b
        # so b depends on a
        a, b = line.split("|")
        deps[int(b)].add(int(a))
    else:
        v = tuple(map(int, line.split(",")))
        updates.append(v)

correctly_ordered_updates = []

for update in updates:
    for i, elt in enumerate(update):
        deps_elt = deps[elt]
        if set(update[i + 1 :]) & deps[elt]:
            break
    else:
        correctly_ordered_updates.append(update)

result = sum(update[len(update) // 2] for update in correctly_ordered_updates)
print(result)
