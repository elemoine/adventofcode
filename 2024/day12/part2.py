from collections import defaultdict

with open("input") as f_:
    map_ = [list(row.strip()) for row in f_]

ymax = len(map_) - 1
xmax = len(map_[0]) - 1

visited = set()

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def within_bounds(pos):
    return pos[0] >= 0 and pos[0] <= ymax and pos[1] >= 0 and pos[1] <= xmax


def form_region(region, letter, pos):
    if pos in visited:
        return region
    if not within_bounds(pos):
        return region
    if map_[pos[0]][pos[1]] != letter:
        return region
    region.add(pos)
    visited.add(pos)
    for dir_ in DIRECTIONS:
        form_region(region, letter, (pos[0] + dir_[0], pos[1] + dir_[1]))
    return region


def area(region):
    return len(region)


def sides(region):
    region_y = sorted(list(region))
    sides_t, sides_b = 0, 0
    y_t, y_b = -1, -1
    x = -2
    for pos in region_y:
        if pos[1] != x + 1:
            y_t = -1
        adj = (pos[0] - 1, pos[1])
        if adj not in region:
            if pos[0] != y_t:
                sides_t += 1
                y_t = pos[0]
        else:
            y_t = -1
        if pos[1] != x + 1:
            y_b = -1
        adj = (pos[0] + 1, pos[1])
        if adj not in region:
            if pos[0] != y_b:
                sides_b += 1
                y_b = pos[0]
        else:
            y_b = -1
        x = pos[1]

    region_x = sorted(list(region), key=lambda p: (p[1], p[0]))
    sides_l, sides_r = 0, 0
    x_l, x_r = -1, -1
    y = -2
    for pos in region_x:
        if pos[0] != y + 1:
            x_l = -1
        adj = (pos[0], pos[1] - 1)
        if adj not in region:
            if pos[1] != x_l:
                sides_l += 1
                x_l = pos[1]
        else:
            x_l = -1
        if pos[0] != y + 1:
            x_r = -1
        adj = (pos[0], pos[1] + 1)
        if adj not in region:
            if pos[1] != x_r:
                sides_r += 1
                x_r = pos[1]
        else:
            x_r = -1
        y = pos[0]

    sides = sides_t + sides_b + sides_l + sides_r
    return sides


regions = defaultdict(list)


for y in range(len(map_)):
    for x in range(len(map_[y])):
        letter = map_[y][x]
        region = form_region(set(), letter, (y, x))
        if region:
            regions[letter].append(region)


result = 0
for letter, regions_ in regions.items():
    for region in regions_:
        a = area(region)
        s = sides(region)
        result += a * s

print(result)
