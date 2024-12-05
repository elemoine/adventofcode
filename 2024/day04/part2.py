with open("input") as f_:
    letters = [row.strip() for row in f_]


def at_(pos):
    y, x = pos

    if y < 0 or y > len(letters) - 1:
        return None

    if x < 0 or x > len(letters[y]) - 1:
        return None

    return letters[y][x]


def x_mas_at_pos(pos):
    results = []
    for step in ((0, 0), (1, 1), (1, 1), (-2, 0), (1, -1), (1, -1)):
        pos = [pos[0] + step[0], pos[1] + step[1]]
        if r := at_(pos):
            results.append(r)
    result = "".join(results)
    return result in ("MASSAM", "SAMSAM", "MASMAS", "SAMMAS")


cnt = 0
for y in range(0, len(letters)):
    for x in range(0, len(letters[y])):
        cnt += int(x_mas_at_pos((y, x)))

print(cnt)
