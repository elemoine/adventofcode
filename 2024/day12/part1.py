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


def perimeter(region):
    p = 0
    for pos in region:
        for dir_ in DIRECTIONS:
            adj = (pos[0] + dir_[0], pos[1] + dir_[1])
            if not within_bounds(adj) or (map_[adj[0]][adj[1]] != map_[pos[0]][pos[1]]):
                p += 1
    return p


regions = defaultdict(list)


for y in range(len(map_)):
    for x in range(len(map_[y])):
        letter = map_[y][x]
        region = form_region(set(), letter, (y, x))
        if region:
            regions[letter].append(region)


result = 0
for letter, regions_ in regions.items():
    print(letter)
    for region in regions_:
        a = area(region)
        p = perimeter(region)
        result += a * p


print(result)
