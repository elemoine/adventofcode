from collections import Counter


def main():
    with open("input") as f:
        ids = [l.strip() for l in f]
    c2, c3 = 0, 0
    for id_ in ids:
        c = Counter(id_)
        values = set(c.values())
        for v in values:
            if v == 2:
                c2 += 1
            elif v == 3:
                c3 += 1
    print(c2 * c3)


if __name__ == "__main__":
    main()
