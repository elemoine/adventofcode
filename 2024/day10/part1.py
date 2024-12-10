directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def valid_pos(map_, pos):
    bounds = (len(map_) - 1, len(map_[0]) - 1)
    return pos[0] >= 0 and pos[0] <= bounds[0] and pos[1] >= 0 and pos[1] <= bounds[1]


def score(map_, pos, visited):
    y, x = pos
    height = map_[y][x]
    if height == 9:
        if pos in visited:
            return 0
        visited.add(pos)
        return 1
    s = 0
    for dir_ in directions:
        next_pos = (pos[0] + dir_[0], pos[1] + dir_[1])
        if not valid_pos(map_, next_pos):
            continue
        if map_[next_pos[0]][next_pos[1]] == height + 1:
            s += score(map_, next_pos, visited)
    return s


def main():
    with open("input") as f_:
        map_ = [list(map(int, row.strip())) for row in f_]
    scores = {}
    for y in range(len(map_)):
        for x in range(len(map_[y])):
            if map_[y][x] == 0:
                scores[(y, x)] = score(map_, (y, x), set())
    print(sum(s for s in scores.values()))


if __name__ == "__main__":
    main()
