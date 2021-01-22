def parse_input(inputfile):
    with open(inputfile) as f:
        data = f.read()
    lines = data.splitlines()
    depth = int(lines[0][7:])
    target = tuple(map(int, lines[1][8:].split(",")))
    return depth, target


def calc_el(pos, map_, target, depth):
    if pos == (0, 0) or pos == target:
        gi = 0
    elif pos[1] == 0:
        gi = pos[0] * 16807
    elif pos[0] == 0:
        gi = pos[1] * 48271
    else:
        assert (pos[0] - 1, pos[1]) in map_
        assert (pos[0], pos[1] - 1) in map_
        gi = map_[(pos[0] - 1, pos[1])] * map_[(pos[0], pos[1] - 1)]
    return (gi + depth) % 20183


def explore(depth, target):
    map_ = {}

    y = 0
    while y <= target[1]:
        x = 0
        while x <= target[0]:
            pos = (x, y)
            assert pos not in map_
            el = calc_el(pos, map_, target, depth)
            map_[pos] = el
            x += 1
        y += 1

    return map_


def display_map(map_):
    y = None
    for pos in sorted(map_.keys(), key=lambda k: (k[1], k[0])):
        if y is not None and pos[1] != y:
            print()
        print(map_[pos], end="")
        y = pos[1]
    print()


def calc_risk(map_):
    r = 0
    for v in map_.values():
        if v == "=":
            r += 1
        if v == "|":
            r += 2
    return r


symbols = {0: ".", 1: "=", 2: "|"}


def main():
    depth, target = parse_input("input")
    map_ = explore(depth, target)
    map_ = {pos: symbols[el % 3] for pos, el in map_.items()}
    display_map(map_)
    risk = calc_risk(map_)
    print(risk)


if __name__ == "__main__":
    main()
