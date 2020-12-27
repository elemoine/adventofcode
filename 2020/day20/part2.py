import math


def parse_tiles(inputfile):
    with open(inputfile) as f:
        data = f.read()
    tile_dict = {}
    tiles = data.split("\n\n")
    for tile in tiles:
        lines = tile.splitlines()
        tile_id = int(lines[0][5:-1])
        tile_data = [list(line) for line in lines[1:]]
        tile_dict[tile_id] = tile_data
    return tile_dict


def empty_tile(lx, ly):
    return [["."] * ly for _ in range(lx)]


def display_tile(tile_data):
    for x in range(len(tile_data)):
        for y in range(len(tile_data[x])):
            print(tile_data[x][y], end="")
        print()


def rotate90(tile_data):
    lx = len(tile_data)
    ly = len(tile_data[0])
    t = empty_tile(lx, ly)
    for x in range(lx):
        for y in range(ly):
            t[y][lx - 1 - x] = tile_data[x][y]
    return t


def flipy(tile_data):
    lx = len(tile_data)
    ly = len(tile_data[0])
    t = empty_tile(lx, ly)
    for x in range(lx):
        for y in range(ly // 2):
            t[x][y] = tile_data[x][ly - 1 - y]
            t[x][ly - 1 - y] = tile_data[x][y]
    return t


def flipx(tile_data):
    lx = len(tile_data)
    ly = len(tile_data[0])
    t = empty_tile(lx, ly)
    for x in range(lx // 2):
        for y in range(ly):
            t[x][y] = tile_data[lx - 1 - x][y]
            t[lx - 1 - x][y] = tile_data[x][y]
    return t


def identity(tile_data):
    return [list(r) for r in tile_data]


def transform(tile_data, *transforms):
    for t in transforms:
        tile_data = t(tile_data)
    return tile_data


def borders(tile_data):
    return [
        tile_data[0],
        [t[-1] for t in tile_data],
        tile_data[-1],
        [t[0] for t in tile_data],
    ]


transforms = (
    (identity,),
    (rotate90,),
    (rotate90, rotate90),
    (rotate90, rotate90, rotate90),
    (rotate90, flipx),
    (rotate90, flipy),
    (flipx,),
    (flipy,),
)


def fit(tile_data1, tile_data2, border_num):
    border1 = borders(tile_data1)[border_num]
    for t in transforms:
        data = transform(tile_data2, *t)
        border2 = borders(data)[(border_num + 2) % 4]
        if border1 == border2:
            return data


def find_neighbors(tile_id, tiles, puzzle):
    tile_data = tiles[tile_id]
    puzzle[tile_id] = [None] * 4
    for border_num in range(4):
        for id_ in tiles:
            if id_ == tile_id:
                continue
            if data := fit(tile_data, tiles[id_], border_num):
                puzzle[tile_id][border_num] = id_
                tiles[id_] = data
                break
    for id_ in puzzle[tile_id]:
        if id_ and id_ not in puzzle:
            find_neighbors(id_, tiles, puzzle)


def solve_puzzle(tiles):
    tile_id = list(tiles.keys())[0]
    tile_id = 3079
    puzzle = {}
    find_neighbors(tile_id, tiles, puzzle)
    return puzzle


def corners(puzzle):
    for tile_id in puzzle:
        if sum(int(n is None) for n in puzzle[tile_id]) == 2:
            yield tile_id


def north_east_corner(puzzle):
    for tile_id in puzzle:
        adjacent_tiles = puzzle[tile_id]
        if adjacent_tiles[0] is None and adjacent_tiles[3] is None:
            return tile_id


def copy_tile_to_image(tile, image, i, j):
    for ti in range(1, len(tile) - 1):
        for tj in range(1, len(tile[ti]) - 1):
            image[i + ti - 1][j + tj - 1] = tile[ti][tj]


def build_image(puzzle, tiles):
    tile_data = list(tiles.values())[0]
    tx, ty = len(tile_data), len(tile_data[0])
    n_tiles = int(math.sqrt(len(tiles)))
    image = empty_tile(n_tiles * (tx - 2), n_tiles * (ty - 2))
    tile_id = north_east_corner(puzzle)
    i, j = 0, 0
    d = 1
    while tile_id:
        copy_tile_to_image(tiles[tile_id], image, i,  j)
        t = puzzle[tile_id][d]
        if t:
            if d == 1:
                j += (ty - 2)
            else:
                j -= (ty - 2)
        else:
            t = puzzle[tile_id][2]
            if t:
                d = (d + 2) % 4
                i += (tx - 2)
        tile_id = t
    return image


monster = """
__________________#_
#____##____##____###
_#__#__#__#__#__#___
""".strip("\n")  # NOQA


def monster_positions(m):
    positions = []
    for i, line in enumerate(m.split("\n")):
        for j, c in enumerate(line):
            if c == "#":
                positions.append((i, j))
    return positions


def main():
    tiles = parse_tiles("input")
    puzzle = solve_puzzle(tiles)
    image = build_image(puzzle, tiles)
    monster_pos = monster_positions(monster)
    found_monsters = False
    for t in transforms:
        img = transform(image, *t)
        for i in range(len(img) - 3):
            for j in range(len(img[i]) - 20):
                if all(img[i + pos[0]][j + pos[1]] == "#" for pos in monster_pos):
                    found_monsters = True
                    for pos in monster_pos:
                        img[i + pos[0]][j + pos[1]] = "."
        if found_monsters:
            break
    cnt = sum(int(cell == "#") for row in img for cell in row)
    print(cnt)


if __name__ == "__main__":
    main()
