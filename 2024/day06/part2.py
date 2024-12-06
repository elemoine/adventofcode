f_ = open("input")

grid = [list(row.strip()) for row in f_]

init_pos = None
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "^":
            init_pos = (y, x)
            break
    if init_pos:
        break


assert init_pos

init_dir = (-1, 0)


def still_in(pos):
    y, x = pos
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])


def turn_right(dir_):
    # the rotation matrix for -pi / 2 is
    # |0   1|
    # |-1  0|
    return (dir_[1], -dir_[0])


def obstacle(pos):
    if still_in(pos):
        return grid[pos[0]][pos[1]] == "#"
    return False


pos, dir_ = init_pos, init_dir
path = set()

while still_in(pos):
    pos_ = (pos[0] + dir_[0], pos[1] + dir_[1])
    if obstacle(pos_):
        dir_ = turn_right(dir_)
    else:
        path.add(pos)
        pos = pos_

loops = 0
for y, x in path:
    assert grid[y][x] != "#"
    if grid[y][x] in ("#", "^"):
        continue

    # (y, x) is the position of the new obstacle
    grid[y][x] = "#"

    pos, dir_ = init_pos, init_dir
    obstacle_visits = set()

    while still_in(pos):
        pos_ = (pos[0] + dir_[0], pos[1] + dir_[1])
        if obstacle(pos_):
            k = (pos_[0], pos_[1], pos[0], pos[1])
            if k in obstacle_visits:
                print("loop detected", y, x)
                loops += 1
                break
            obstacle_visits.add(k)
            dir_ = turn_right(dir_)
        else:
            pos = pos_

    grid[y][x] = "."

print(loops)
