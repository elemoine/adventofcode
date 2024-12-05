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
        v = list(map(int, line.split(",")))
        updates.append(v)

incorrectly_ordered_updates = []

for update in updates:
    for i, elt in enumerate(update):
        if set(update[i + 1 :]) & deps[elt]:
            incorrectly_ordered_updates.append(update)
            break

for update in incorrectly_ordered_updates:
    i = 0
    while i < len(update):
        elt = update[i]
        for other in update[i + 1 :]:
            if other in deps[elt]:
                j = update.index(other)
                update[i] = other
                update[j] = elt
                break
        else:
            i += 1

result = sum(update[len(update) // 2] for update in incorrectly_ordered_updates)
print(result)
