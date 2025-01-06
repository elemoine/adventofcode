def display(pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            print(pattern[i][j], end="")
        print()
    print()


def clone(pattern):
    return [row.copy() for row in pattern]


def find_reflection(pattern, skip=-1):
    # search horizontally
    pattern_y = pattern
    for y in range(len(pattern_y) - 1):
        y1, y2 = y, y + 1
        while y1 >= 0 and y2 < len(pattern_y):
            if pattern_y[y1] != pattern_y[y2]:
                break
            y1 -= 1
            y2 += 1
        else:
            r = (y + 1) * 100
            if r != skip:
                return r

    # search vertically
    pattern_x = list(map(list, zip(*pattern)))
    for x in range(len(pattern_x) - 1):
        x1, x2 = x, x + 1
        while x1 >= 0 and x2 < len(pattern_x):
            if pattern_x[x1] != pattern_x[x2]:
                break
            x1 -= 1
            x2 += 1
        else:
            r = x + 1
            if r != skip:
                return r

    return 0


def find_reflection_with_flip(pattern, i):
    r1 = find_reflection(pattern)
    # display(pattern)
    for y in range(len(pattern)):
        for x in range(len(pattern[y])):
            p = clone(pattern)
            p[y][x] = "#" if p[y][x] == "." else "."
            r = find_reflection(p, skip=r1)
            if r and r != r1:
                return r
    assert False


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

r = sum(find_reflection_with_flip(pattern, i) for i, pattern in enumerate(patterns))
print(r)
