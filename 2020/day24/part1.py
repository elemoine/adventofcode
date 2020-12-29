import re


def parse_directions(inputfile):
    with open(inputfile) as f:
        data = f.read()
    directions = []
    for line in data.splitlines():
        line = line.strip()
        d = []
        while line:
            m = re.match(r"^(se|sw|ne|nw|e|w).*$", line)
            d.append(m.group(1))
            line = line[len(m.group(1)):]
        directions.append(d)
    return directions


directional_offsets = {
    "se": ((-1, -1), (0, -1)),
    "sw": ((0, -1), (1, -1)),
    "ne": ((-1, 1), (0, 1)),
    "nw": ((0, 1), (1, 1)),
    "e": ((-1, 0), (-1, 0)),
    "w": ((1, 0), (1, 0)),
}


def main():
    directions = parse_directions("input")

    # use "odd-r" horizontal layout
    # see https://www.redblobgames.com/grids/hexagons/

    black = set()
    ref = (0, 0)
    for direction in directions:
        tile = tuple(ref)
        for d in direction:
            offset = directional_offsets[d][int(tile[1] % 2 == 0)]
            tile = (tile[0] + offset[0], tile[1] + offset[1])
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)
    print(len(black))


if __name__ == "__main__":
    main()
