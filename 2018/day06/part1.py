import collections


def readpositions(inputfile):
    positions = {}
    with open(inputfile) as f:
        for i, l in enumerate(f):
            x, y = tuple(map(int, l.strip().split(",")))
            positions[(x, y)] = i
    return positions


def distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def main():
    positions = readpositions("input")
    xs, ys = zip(*positions)
    minx, miny = min(xs), min(ys)
    maxx, maxy = max(xs), max(ys)
    dmap = {}
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            for pos, name in positions.items():
                d = distance(pos, (x, y))
                if (x, y) not in dmap:
                    dmap[(x, y)] = (name, d)
                elif d < dmap[(x, y)][1]:
                    dmap[(x, y)] = (name, d)
                elif d == dmap[(x, y)][1]:
                    dmap[(x, y)] = (".", d)
            assert (x, y) in dmap
    top = map(lambda pos: dmap[pos][0], filter(lambda pos: pos[1] == miny, dmap))
    rig = map(lambda pos: dmap[pos][0], filter(lambda pos: pos[0] == maxx, dmap))
    bot = map(lambda pos: dmap[pos][0], filter(lambda pos: pos[1] == maxy, dmap))
    lef = map(lambda pos: dmap[pos][0], filter(lambda pos: pos[0] == minx, dmap))
    finite = set(positions.values()) - set(top) - set(rig) - set(bot) - set(lef)
    c = collections.Counter()
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            assert (x, y) in dmap
            name = dmap[(x, y)][0]
            if name in finite:
                c[name] += 1
    print(c.most_common(1))


if __name__ == "__main__":
    main()
