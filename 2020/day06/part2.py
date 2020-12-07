def intersection(sets):
    r = None
    for s in sets:
        r = s if r is None else r & s
    return r


def main():
    with open("input") as f:
        data = f.read().split("\n\n")
    groups = [map(set, g.strip().split("\n")) for g in data]
    print(sum(len(intersection(g)) for g in groups))


if __name__ == "__main__":
    main()
