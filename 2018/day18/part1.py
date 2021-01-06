def read_area(inputfile):
    with open(inputfile) as f:
        return [list(row.strip()) for row in f]


def display_area(area):
    for row in area:
        print("".join(row))


def adjacent_acres(acre, area):
    size = len(area)
    for d in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
        x = acre[0] + d[0]
        y = acre[1] + d[1]
        if (0 <= x < size) and (0 <= y < size):
            yield area[x][y]


def empty_area(size):
    return [["."] * size for _ in range(size)]


def change(area):
    size = len(area)
    new_area = empty_area(size)
    for x in range(len(area)):
        for y in range(len(area[x])):
            if area[x][y] == ".":
                if sum(int(a == "|") for a in adjacent_acres((x, y), area)) >= 3:
                    new_area[x][y] = "|"
                else:
                    new_area[x][y] = area[x][y]
            if area[x][y] == "|":
                if sum(int(a == "#") for a in adjacent_acres((x, y), area)) >= 3:
                    new_area[x][y] = "#"
                else:
                    new_area[x][y] = area[x][y]
            if area[x][y] == "#":
                if (
                    sum(int(a == "#") for a in adjacent_acres((x, y), area)) >= 1
                    and sum(int(a == "|") for a in adjacent_acres((x, y), area)) >= 1
                ):
                    new_area[x][y] = area[x][y]
                else:
                    new_area[x][y] = "."
    return new_area


def main():
    area = read_area("input")
    minutes = 10
    for _ in range(minutes):
        area = change(area)
    result = sum(int(c == "#") for r in area for c in r) * sum(
        int(c == "|") for r in area for c in r
    )
    print(result)


if __name__ == "__main__":
    main()
