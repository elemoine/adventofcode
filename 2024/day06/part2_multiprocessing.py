import multiprocessing

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


assert init_pos is not None

init_dir = (-1, 0)


def still_in(pos, grid):
    y, x = pos
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])


def turn_right(dir_):
    # the rotation matrix for -pi / 2 is
    # |0   1|
    # |-1  0|
    return (dir_[1], -dir_[0])


def obstacle(pos, grid):
    if still_in(pos, grid):
        return grid[pos[0]][pos[1]] == "#"
    return False


pos, dir_ = init_pos, init_dir
path = set()

while still_in(pos, grid):
    pos_ = (pos[0] + dir_[0], pos[1] + dir_[1])
    if obstacle(pos_, grid):
        dir_ = turn_right(dir_)
    else:
        path.add(pos)
        pos = pos_


def clone_grid():
    clone = grid.copy()
    for y in range(len(clone)):
        clone[y] = clone[y].copy()
    return clone


def find_cycle(pos):
    y, x = pos

    grid_ = clone_grid()

    assert grid_[y][x] != "#"

    if grid_[y][x] == "^":
        return 0

    # (y, x) is the position of the new obstacle
    grid_[y][x] = "#"

    pos, dir_ = init_pos, init_dir
    obstacle_visits = set()

    while still_in(pos, grid_):
        pos_ = (pos[0] + dir_[0], pos[1] + dir_[1])
        if obstacle(pos_, grid_):
            k = (pos_[0], pos_[1], pos[0], pos[1])
            if k in obstacle_visits:
                return 1
            obstacle_visits.add(k)
            dir_ = turn_right(dir_)
        else:
            pos = pos_

    grid_[y][x] = "."

    return 0


if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        loops = pool.map(find_cycle, path)

    print(sum(loops))
