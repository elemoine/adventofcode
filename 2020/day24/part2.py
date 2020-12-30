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


def adjacent_tiles(tile):
    i = int(tile[1] % 2 == 0)
    for o in directional_offsets.values():
        yield (tile[0] + o[i][0], tile[1] + o[i][1])


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

    for _ in range(100):
        flip_white, flip_black = set(), set()
        for tile in black:
            n_adjacents_black = sum(int(t in black) for t in adjacent_tiles(tile))
            if n_adjacents_black == 0 or n_adjacents_black > 2:
                flip_white.add(tile)
            for t in adjacent_tiles(tile):
                if t in black:
                    continue
                n_adjacents_black = sum(int(a in black) for a in adjacent_tiles(t))
                assert n_adjacents_black > 0
                if n_adjacents_black == 2:
                    flip_black.add(t)
        black -= flip_white
        black |= flip_black

    print(len(black))


if __name__ == "__main__":
    main()
