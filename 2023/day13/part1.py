def display(pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            print(pattern[i][j], end="")
        print()
    print()
                    
patterns = []

with open("input") as f_:
    pattern = []
    patterns.append(pattern)
    for row in f_:
        row = row.strip()
        if row == "":
            pattern = []
            patterns.append(pattern)
        else:
            pattern.append(list(row))

r = 0

for i, pattern in enumerate(patterns):
    # search horizontally
    pattern_y, sym_y = pattern, None
    for y in range(len(pattern_y) - 1):
        y1, y2 = y, y + 1
        while y1 >= 0 and y2 < len(pattern_y):
            if pattern_y[y1] != pattern_y[y2]:
                break
            y1 -= 1
            y2 += 1
        else:
            sym_y = y
            break

    if sym_y is not None:
        r += (sym_y + 1) * 100
        continue

    # search vertically
    pattern_x, sym_x = list(map(list, zip(*pattern))), None
    for x in range(len(pattern_x) - 1):
        x1, x2 = x, x + 1
        while x1 >= 0 and x2 < len(pattern_x):
            if pattern_x[x1] != pattern_x[x2]:
                break
            x1 -= 1
            x2 += 1
        else:
            sym_x = x
            break

    assert sym_x is not None
    r += sym_x + 1

print(r)
