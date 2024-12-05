directions = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]
assert len(directions) == 8

with open("input") as f_:
    letters = [row.strip() for row in f_]


def is_(pos, char):
    y, x = pos

    if y < 0 or y > len(letters) - 1:
        return False

    if x < 0 or x > len(letters[y]) - 1:
        return False

    return letters[y][x] == char


def xmas_at_pos(pos):
    if not is_(pos, "X"):
        return 0

    cnt = 0

    for dir_ in directions:
        next_pos = pos
        for letter in ("M", "A", "S"):
            next_pos = (next_pos[0] + dir_[0], next_pos[1] + dir_[1])
            if not is_(next_pos, letter):
                break
        else:
            cnt += 1

    return cnt


cnt = 0
for y in range(0, len(letters)):
    for x in range(0, len(letters[y])):
        pos = (y, x)
        cnt += xmas_at_pos(pos)

print(cnt)
