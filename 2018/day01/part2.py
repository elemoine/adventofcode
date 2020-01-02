import itertools


def main():
    with open("input") as f:
        seq = [int(l.strip()) for l in f]
    s = set()
    f = 0
    for c in itertools.cycle(seq):
        f += c
        if f in s:
            return f
        s.add(f)


if __name__ == "__main__":
    print(main())
