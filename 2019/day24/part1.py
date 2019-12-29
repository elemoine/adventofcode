def readarea(inputfile):
    area = []
    with open(inputfile) as f:
        for l in f:
            area.append(list(l.strip()))
    return area


def play(area):
    newarea = []
    for r in range(len(area)):
        line = []
        for c in range(len(area[r])):
            bugs = 0
            if r > 0 and area[r - 1][c] == "#":
                bugs += 1
            if r < len(area) - 1 and area[r + 1][c] == "#":
                bugs += 1
            if c > 0 and area[r][c - 1] == "#":
                bugs += 1
            if c < len(area[r]) - 1 and area[r][c + 1] == "#":
                bugs += 1
            if area[r][c] == "#":
                char = "#" if bugs == 1 else "."
            else:
                assert area[r][c] == "."
                char = "#" if bugs in (1, 2) else "."
            line.append(char)
        newarea.append(line)
    return newarea


def displayarea(area):
    for l in area:
        for c in l:
            print(c, end="")
        print()


def main(inputfile):
    area = readarea(inputfile)
    stored = [area]
    while True:
        area = play(area)
        for s in stored:
            if area == s:
                break
        else:
            stored.append(area)
            continue
        break
    displayarea(area)

    def gen():
        for r in range(len(area)):
            for c in range(len(area[r])):
                if area[r][c] == "#":
                    yield r * len(area[r]) + c

    print(sum(2**n for n in gen()))


if __name__ == "__main__":
    main("input")
