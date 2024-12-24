from collections import Counter

with open("input") as f_:
    codes = [row.strip() for row in f_]

nkeyp = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
dkeyp = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}


def steps(keyp, code, n=1):
    x, y = keyp["A"]
    gx, gy = keyp[" "]
    r = Counter()
    for c in code:
        nx, ny = keyp[c]
        g = nx == gx and y == gy or x == gx and ny == gy
        r[(nx - x, ny - y, g)] += n
        x, y = nx, ny
    return r


n = 25

result = 0
for code in codes:
    r = steps(nkeyp, code)
    for _ in range(n + 1):
        r = sum(
            (
                steps(
                    dkeyp,
                    ("<" * -x + "v" * y + "^" * -y + ">" * x)[:: -1 if g else 1] + "A",
                    r[(x, y, g)],
                )
                for x, y, g in r
            ),
            start=Counter(),
        )
    result += r.total() * int(code[:3])

print(result)
