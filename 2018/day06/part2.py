def readpositions(inputfile):
    positions = {}
    with open(inputfile) as f:
        for i, l in enumerate(f):
            x, y = tuple(map(int, l.strip().split(",")))
            positions[(x, y)] = i
    return positions


def distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def main(inputfile, max_):
    positions = readpositions(inputfile)
    xs, ys = zip(*positions)
    minx, miny = min(xs), min(ys)
    maxx, maxy = max(xs), max(ys)
    size = 0
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            d = 0
            for pos in positions:
                d += distance(pos, (x, y))
            if d < max_:
                size += 1
    print(size)


if __name__ == "__main__":
    main("input", 10000)
