with open("input") as f_:
    codes = [row.strip() for row in f_]

nkeyp = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
dkeyp = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}

N = 25


def moves(keyp, code):
    x, y = keyp["A"]
    gx, gy = keyp[" "]
    for c in code:
        nx, ny = keyp[c]
        g = nx == gx and y == gy or x == gx and ny == gy
        yield (nx - x, ny - y, g)
        x, y = nx, ny


def move_code(dx, dy, g):
    return ("<" * -dx + "v" * dy + "^" * -dy + ">" * dx)[:: -1 if g else 1] + "A"


def code_length(code, level=0, cache={}):
    if level == N + 1:
        return len(code)
    k = (code, level)
    if k in cache:
        return cache[k]
    keyp = nkeyp if level == 0 else dkeyp
    l_ = sum(
        code_length(move_code(x, y, g), level + 1, cache)
        for x, y, g in moves(keyp, code)
    )
    cache[k] = l_
    return l_


result = sum(code_length(c) * int(c[:3]) for c in codes)
print(result)
