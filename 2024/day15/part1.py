DIRECTIONS = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}

DIRECTIONS_ = {
    (0, -1): "<",
    (-1, 0): "^",
    (0, 1): ">",
    (1, 0): "v",
}

with open("input") as f_:
    rows = [row.strip() for row in f_]

map_ = []
directions = []
map_complete = False

for row in rows:
    if row == "":
        map_complete = True
        continue
    if map_complete:
        directions.extend(list(map(lambda c: DIRECTIONS[c], row)))
    else:
        map_.append(list(row))


def move(from_, dir_, char="@"):
    fy, fx = from_
    ty, tx = (fy + dir_[0], fx + dir_[1])
    if map_[ty][tx] == "O":
        move((ty, tx), dir_, "O")
    if map_[ty][tx] == ".":
        map_[ty][tx] = char
        map_[fy][fx] = "."
        return (ty, tx)
    return (fy, fx)


def display():
    for y in range(len(map_)):
        for x in range(len(map_[y])):
            c = map_[y][x]
            print(c, end="")
        print()
    print()


robot = next(
    (y, x) for y in range(len(map_)) for x in range(len(map_[y])) if map_[y][x] == "@"
)

# display()

for dir_ in directions:
    robot = move(robot, dir_)
    # print(f"Move {DIRECTIONS_[dir_]}:")
    # display()

# display()


result = sum(
    100 * y + x
    for y in range(len(map_))
    for x in range(len(map_[y]))
    if map_[y][x] == "O"
)
print(result)
