f_ = open("input")

grid = [list(row.strip()) for row in f_]

pos = None
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "^":
            pos = (y, x)
            break
    if pos:
        break


assert pos


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


dir_ = (-1, 0)
visits = set()

while still_in(pos):
    pos_ = (pos[0] + dir_[0], pos[1] + dir_[1])
    if obstacle(pos_):
        dir_ = turn_right(dir_)
    else:
        visits.add(pos)
        pos = pos_

print(len(visits))
