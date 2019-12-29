adjacent = {
    (0, 0): ((-1, 1, 2), (0, 0, 1), (0, 1, 0), (-1, 2, 1)),
    (0, 1): ((-1, 1, 2), (0, 0, 2), (0, 1, 1), (0, 0, 0)),
    (0, 2): ((-1, 1, 2), (0, 0, 3), (0, 1, 2), (0, 0, 1)),
    (0, 3): ((-1, 1, 2), (0, 0, 4), (0, 1, 3), (0, 0, 2)),
    (0, 4): ((-1, 1, 2), (-1, 2, 3), (0, 1, 4), (0, 0, 3)),
    (1, 0): ((0, 0, 0), (0, 1, 1), (0, 2, 0), (-1, 2, 1)),
    (1, 1): ((0, 0, 1), (0, 1, 2), (0, 2, 1), (0, 1, 0)),
    (1, 2): ((0, 0, 2), (0, 1, 3), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 0, 4), (0, 1, 1)),
    (1, 3): ((0, 0, 3), (0, 1, 4), (0, 2, 3), (0, 1, 2)),
    (1, 4): ((0, 0, 4), (-1, 2, 3), (0, 2, 4), (0, 1, 3)),
    (2, 0): ((0, 1, 0), (0, 2, 1), (0, 3, 0), (-1, 2, 1)),
    (2, 1): ((0, 1, 1), (1, 0, 0), (1, 1, 0), (1, 2, 0), (1, 3, 0), (1, 4, 0), (0, 3, 1), (0, 2, 0)),
    (2, 2): None,
    (2, 3): ((0, 1, 3), (0, 2, 4), (0, 3, 3), (1, 0, 4), (1, 1, 4), (1, 2, 4), (1, 3, 4), (1, 4, 4)),
    (2, 4): ((0, 1, 4), (-1, 2, 3), (0, 3, 4), (0, 2, 3)),
    (3, 0): ((0, 2, 0), (0, 3, 1), (0, 4, 0), (-1, 2, 1)),
    (3, 1): ((0, 2, 1), (0, 3, 2), (0, 4, 1), (0, 3, 0)),
    (3, 2): ((1, 4, 0), (1, 4, 1), (1, 4, 2), (1, 4, 3), (1, 4, 4), (0, 3, 3), (0, 4, 2), (0, 3, 1)),
    (3, 3): ((0, 2, 3), (0, 3, 4), (0, 4, 3), (0, 3, 2)),
    (3, 4): ((0, 2, 4), (-1, 2, 3), (0, 4, 4), (0, 3, 3)),
    (4, 0): ((0, 3, 0), (0, 4, 1), (-1, 3, 2), (-1, 2, 1)),
    (4, 1): ((0, 3, 1), (0, 4, 2), (-1, 3, 2), (0, 4, 0)),
    (4, 2): ((0, 3, 2), (0, 4, 3), (-1, 3, 2), (0, 4, 1)),
    (4, 3): ((0, 3, 3), (0, 4, 4), (-1, 3, 2), (0, 4, 2)),
    (4, 4): ((0, 3, 4), (-1, 2, 3), (-1, 3, 2), (0, 4, 3)),
}


def readarea(inputfile):
    area = []
    with open(inputfile) as f:
        for l in f:
            area.append(list(l.strip()))
    area[2][2] = "?"
    return area


def displayarea(area):
    for l in area:
        for c in l:
            print(c, end="")
        print()


def displayareas(areas):
    keys = sorted(areas.keys())
    for k in keys:
        print("area level", k)
        displayarea(areas[k])
        print()


def play(areas, nobugsarea):
    levels = list(areas.keys())
    for level in levels:
        assert level in areas
        if level - 1 not in areas:
            areas[level - 1] = nobugsarea
        if level + 1 not in areas:
            areas[level + 1] = nobugsarea
    newareas = {}
    for level, area in areas.items():
        newareas[level] = []
        for r in range(len(area)):
            line = []
            for c in range(len(area[r])):
                if (r, c) == (2, 2):
                    line.append("?")
                    continue
                bugs = 0
                assert (r, c) != (2, 2)
                for ll, lr, lc in adjacent[(r, c)]:
                    assert (lr, lc) != (2, 2)
                    ll += level
                    if ll in areas and areas[ll][lr][lc] == "#":
                        bugs += 1
                if area[r][c] == "#":
                    char = "#" if bugs == 1 else "."
                else:
                    assert area[r][c] == "."
                    char = "#" if bugs in (1, 2) else "."
                line.append(char)
            newareas[level].append(line)
    for k in list(newareas.keys()):
        if newareas[k] == nobugsarea:
            del newareas[k]
    return newareas


def numbugs(areas):
    cnt = 0
    for level, area in areas.items():
        for l in area:
            for c in l:
                if c == "#":
                    cnt += 1
    return cnt


def main(inputfile, n):
    nobugsarea = [["." for _ in range(5)] for _ in range(5)]
    nobugsarea[2][2] = "?"
    area = readarea(inputfile)
    areas = {0: area}
    for t in range(n):
        areas = play(areas, nobugsarea)
    print(numbugs(areas))


if __name__ == "__main__":
    main("testinput0", 10)
    main("input", 200)
