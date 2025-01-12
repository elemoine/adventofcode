import sys

with open("input") as f_:
    layout = [list(row.strip()) for row in f_]


def run(pos, dir_, seen):
    y, x = pos
    if y < 0 or y >= len(layout) or x < 0 or x >= len(layout[y]):
        return
    # detect cycles
    if (pos, dir_) in seen:
        return
    seen.add((pos, dir_))
    if layout[y][x] == ".":
        run((pos[0] + dir_[0], pos[1] + dir_[1]), dir_, seen)
        return
    if layout[y][x] == "-":
        if dir_[0] == 0:
            assert dir_[1] in (-1, 1)
            run((pos[0] + dir_[0], pos[1] + dir_[1]), dir_, seen)
        else:
            assert dir_[0] in (-1, 1)
            run((pos[0], pos[1] + 1), (0, 1), seen)
            run((pos[0], pos[1] - 1), (0, -1), seen)
        return
    if layout[y][x] == "|":
        if dir_[1] == 0:
            assert dir_[0] in (-1, 1)
            run((pos[0] + dir_[0], pos[1] + dir_[1]), dir_, seen)
        else:
            assert dir_[1] in (-1, 1)
            run((pos[0] + 1, pos[1]), (1, 0), seen)
            run((pos[0] - 1, pos[1]), (-1, 0), seen)
        return
    if layout[y][x] == "\\":
        if dir_[1] == 1:
            run((pos[0] + 1, pos[1]), (1, 0), seen)
        elif dir_[1] == -1:
            run((pos[0] - 1, pos[1]), (-1, 0), seen)
        elif dir_[0] == 1:
            run((pos[0], pos[1] + 1), (0, 1), seen)
        else:
            assert dir_[0] == -1
            run((pos[0], pos[1] - 1), (0, -1), seen)
    if layout[y][x] == "/":
        if dir_[1] == 1:
            run((pos[0] - 1, pos[1]), (-1, 0), seen)
        elif dir_[1] == -1:
            run((pos[0] + 1, pos[1]), (1, 0), seen)
        elif dir_[0] == 1:
            run((pos[0], pos[1] - 1), (0, -1), seen)
        else:
            assert dir_[0] == -1
            run((pos[0], pos[1] + 1), (0, 1), seen)


sys.setrecursionlimit(6000)  # oops

r = 0
for y in range(len(layout)):
    for x in range(len(layout[y])):
        if y > 0 and y < len(layout) - 1 and x > 0 and x < len(layout[y]) - 1:
            continue
        pos = y, x
        if y == 0:
            seen = set()
            run((y, x), (1, 0), seen)
            energized = {e[0] for e in seen}
            r = max(r, len(energized))
        elif y == len(layout) - 1:
            seen = set()
            run((y, x), (-1, 0), seen)
            energized = {e[0] for e in seen}
            r = max(r, len(energized))
        if x == 0:
            seen = set()
            run((y, x), (0, 1), seen)
            energized = {e[0] for e in seen}
            r = max(r, len(energized))
        elif x == len(layout[y]) - 1:
            seen = set()
            run((y, x), (0, -1), seen)
            energized = {e[0] for e in seen}
            r = max(r, len(energized))

print(r)
