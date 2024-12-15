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
    elif map_complete:
        directions.extend(list(map(lambda c: DIRECTIONS[c], row)))
    else:
        map_.append(list(row))


def can_move_box_vert(from_, dir_):
    # test if a box can be moved up or down
    assert dir_ in ((-1, 0), (1, 0))

    fy, fx = from_

    # check that it’s a box
    assert map_[fy][fx] == "["
    assert map_[fy][fx + 1] == "]"

    ty, tx = (fy + dir_[0], fx + dir_[1])

    if map_[ty][tx] == "#" or map_[ty][tx + 1] == "#":
        return False

    if map_[ty][tx] == "." and map_[ty][tx + 1] == ".":
        return True

    if map_[ty][tx] == "[":
        assert map_[ty][tx + 1] == "]"
        return can_move_box_vert((ty, tx), dir_)

    left_ok = map_[ty][tx] == "."
    if not left_ok:
        left_ok = can_move_box_vert((ty, tx - 1), dir_)

    right_ok = map_[ty][tx + 1] == "."
    if not right_ok:
        right_ok = can_move_box_vert((ty, tx + 1), dir_)

    return left_ok and right_ok


def move_box_vert(from_, dir_):
    # test if a box can be moved up or down
    assert dir_ in ((-1, 0), (1, 0))

    fy, fx = from_

    # check that it’s a box
    assert map_[fy][fx] == "["
    assert map_[fy][fx + 1] == "]"

    ty, tx = (fy + dir_[0], fx + dir_[1])

    if map_[ty][tx] == "#" or map_[ty][tx + 1] == "#":
        return (fy, fx)

    if map_[ty][tx] == "[":
        assert map_[ty][tx + 1] == "]"
        move_box_vert((ty, tx), dir_)

    if map_[ty][tx] == "]":
        assert map_[ty][tx - 1] == "["
        move_box_vert((ty, tx - 1), dir_)

    if map_[ty][tx + 1] == "[":
        assert map_[ty][tx + 2] == "]"
        move_box_vert((ty, tx + 1), dir_)

    if map_[ty][tx] == "." and map_[ty][tx + 1] == ".":
        map_[ty][tx] = "["
        map_[ty][tx + 1] = "]"
        map_[fy][fx] = "."
        map_[fy][fx + 1] = "."
        return (ty, tx)

    assert False


def move(from_, dir_, char="@"):
    fy, fx = from_
    ty, tx = (fy + dir_[0], fx + dir_[1])

    if dir_ == (0, -1) and map_[ty][tx] == "]":
        # push box left
        assert map_[ty][tx - 1] == "["
        move((ty, tx - 1), dir_, "[")

    elif dir_ == (0, 1) and map_[ty][tx] == "[":
        # push box  right
        assert map_[ty][tx + 1] == "]"
        move((ty, tx + 1), dir_, "]")

    elif dir_ == (-1, 0) and map_[ty][tx] == "[":
        # puth box up
        assert map_[ty][tx + 1] == "]"
        if can_move_box_vert((ty, tx), dir_):
            move_box_vert((ty, tx), dir_)

    elif dir_ == (-1, 0) and map_[ty][tx] == "]":
        # puth box up
        assert map_[ty][tx - 1] == "["
        if can_move_box_vert((ty, tx - 1), dir_):
            move_box_vert((ty, tx - 1), dir_)

    elif dir_ == (1, 0) and map_[ty][tx] == "[":
        # push bow down
        assert map_[ty][tx + 1] == "]"
        if can_move_box_vert((ty, tx), dir_):
            move_box_vert((ty, tx), dir_)

    elif dir_ == (1, 0) and map_[ty][tx] == "]":
        # push bow down
        assert map_[ty][tx - 1] == "["
        if can_move_box_vert((ty, tx - 1), dir_):
            move_box_vert((ty, tx - 1), dir_)

    if map_[ty][tx] == ".":
        if char == "@":
            map_[ty][tx] = "@"
            map_[fy][fx] = "."
        elif dir_ == (0, -1):
            assert char == "["
            map_[ty][tx] = "["
            map_[ty][tx + 1] = "]"
            map_[ty][tx + 2] = "."
        elif dir_ == (0, 1):
            assert char == "]"
            map_[ty][tx] = "]"
            map_[ty][tx - 1] = "["
            map_[ty][tx - 2] = "."
        return (ty, tx)

    return (fy, fx)


def doublemap():
    for y in range(len(map_)):
        row = []
        for x in range(len(map_[y])):
            if map_[y][x] == "#":
                row.extend(["#", "#"])
            elif map_[y][x] == ".":
                row.extend([".", "."])
            elif map_[y][x] == "O":
                row.extend(["[", "]"])
            elif map_[y][x] == "@":
                row.extend(["@", "."])
        map_[y] = row


def display():
    for y in range(len(map_)):
        for x in range(len(map_[y])):
            c = map_[y][x]
            print(c, end="")
        print()
    print()


doublemap()

robot = next(
    (y, x) for y in range(len(map_)) for x in range(len(map_[y])) if map_[y][x] == "@"
)

# display()

for dir_ in directions:
    # print(f"Move {DIRECTIONS_[dir_]}:")
    robot = move(robot, dir_)
    # display()

# display()

result = sum(
    100 * y + x
    for y in range(len(map_))
    for x in range(len(map_[y]))
    if map_[y][x] == "["
)
print(result)
