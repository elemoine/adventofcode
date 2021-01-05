def parse_scan(inputfile):
    with open(inputfile) as f:
        data = f.read()
    scan = {}
    for line in data.splitlines():
        xv, yv = None, None
        for coord in line.strip().split(", "):
            c, v = coord.split("=")
            v = v.split("..")
            if len(v) == 1:
                v = range(int(v[0]), int(v[0]) + 1)
            else:
                v = range(int(v[0]), int(v[1]) + 1)
            if c == "x":
                xv = v
            else:
                assert c == "y"
                yv = v
        for y in yv:
            for x in xv:
                scan[(y, x)] = "#"
    min_y = min(map(lambda e: e[0], scan.keys())) - 1
    max_y = max(map(lambda e: e[0], scan.keys())) + 1
    min_x = min(map(lambda e: e[1], scan.keys())) - 1
    max_x = max(map(lambda e: e[1], scan.keys())) + 1
    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) not in scan:
                scan[(y, x)] = "."
    return scan, min_y + 1, max_y - 1


def display_scan(scan):
    p = None
    for key in sorted(scan.keys()):
        if p is not None and key[0] != p:
            print()
        print(scan[key], end="")
        p = key[0]
    print()


def add_water(pos, scan, max_y, level):
    y, x = pos
    while True:
        if y > max_y:
            break
        if scan[(y, x)] in (".", "|"):
            scan[(y, x)] = "|"
            y += 1
            continue
        assert scan[(y, x)] in ("#", "~")
        left = x - 1
        while scan[(y - 1, left)] != "#" and scan[(y, left)] not in (".", "|"):
            left -= 1
        right = x + 1
        while scan[(y - 1, right)] != "#" and scan[(y, right)] not in (".", "|"):
            right += 1
        if scan[(y - 1, left)] == "#" and scan[(y - 1, right)] == "#":
            for i in range(left + 1, right):
                scan[(y - 1, i)] = "~"
        else:
            if scan[(y, left)] == "|" or scan[(y, right)] == "|":
                break
            if scan[(y, left)] == ".":
                for i in range(left, right):
                    scan[(y - 1, i)] = "|"
                add_water((y, left), scan, max_y, level + 1)
            if scan[(y, right)] == ".":
                for i in range(left + 1, right + 1):
                    scan[(y - 1, i)] = "|"
                add_water((y, right), scan, max_y, level + 1)
        y, x = pos
        if scan[(y, x)] == "~":
            break


def main():
    scan, min_y, max_y = parse_scan("input")
    add_water((1, 500), scan, max_y, 1)
    display_scan(scan)
    result = sum(int(v in ("|", "~")) for k, v in scan.items() if min_y <= k[0] <= max_y)
    print(result)
    result = sum(int(v == "~") for k, v in scan.items() if min_y <= k[0] <= max_y)
    print(result)


if __name__ == "__main__":
    main()
