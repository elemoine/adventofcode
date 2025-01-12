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

seen = set()
run((0, 0), (0, 1), seen)

energized = {e[0] for e in seen}
print(len(energized))
