def dest(cur, max_, excludes):
    while True:
        cur -= 1
        if cur == 0:
            cur = max_
        if cur not in excludes:
            return cur


def main():
    size = 1_000_000
    iterations = 10_000_000
    cups_str = "364297581"
    cups = [None] * size
    cur = int(cups_str[0])
    i = cur
    for c in cups_str[1:]:
        n = int(c)
        cups[i - 1] = n
        i = n
    for c in range(len(cups_str) + 1, size + 1):
        cups[i - 1] = c
        i = c
    cups[i - 1] = cur
    for _ in range(iterations):
        values = [
            cups[cur - 1],
            cups[cups[cur - 1] - 1],
            cups[cups[cups[cur - 1] - 1] - 1],
        ]
        d = dest(cur, len(cups), set(values))
        n = cups[d - 1]
        cups[d - 1] = values[0]
        m = cups[values[2] - 1]
        cups[values[2] - 1] = n
        cups[cur - 1] = m
        cur = m
    print(cups[0], cups[cups[0] - 1], cups[0] * cups[cups[0] - 1])


if __name__ == "__main__":
    main()
