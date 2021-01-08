def read_directions(inputfile):
    with open(inputfile) as f:
        directions = f.read().strip()
    return directions


def _draw_map(directions, map_, pos, dist=0):
    i = 0
    while i < len(directions):
        d = directions[i]
        if d == "E":
            pos = (pos[0], pos[1] + 2)
            dist += 1
            map_[pos] = min(map_.get(pos, dist), dist)
            map_[(pos[0], pos[1] - 1)] = "|"
            map_.setdefault((pos[0] - 1, pos[1] + 0), "?")
            map_[(pos[0] - 1, pos[1] + 1)] = "#"
            map_.setdefault((pos[0] + 0, pos[1] + 1), "?")
            map_[(pos[0] + 1, pos[1] + 1)] = "#"
            map_.setdefault((pos[0] + 1, pos[1] + 0), "?")
        elif d == "N":
            pos = (pos[0] - 2, pos[1])
            dist += 1
            map_[pos] = min(map_.get(pos, dist), dist)
            map_[(pos[0] + 1, pos[1])] = "-"
            map_.setdefault((pos[0] + 0, pos[1] - 1), "?")
            map_[(pos[0] - 1, pos[1] - 1)] = "#"
            map_.setdefault((pos[0] - 1, pos[1] + 0), "?")
            map_[(pos[0] - 1, pos[1] + 1)] = "#"
            map_.setdefault((pos[0] + 0, pos[1] + 1), "?")
        elif d == "W":
            pos = (pos[0], pos[1] - 2)
            dist += 1
            map_[pos] = min(map_.get(pos, dist), dist)
            map_[(pos[0], pos[1] + 1)] = "|"
            map_.setdefault((pos[0] + 1, pos[1] + 0), "?")
            map_[(pos[0] + 1, pos[1] - 1)] = "#"
            map_.setdefault((pos[0] + 0, pos[1] - 1), "?")
            map_[(pos[0] - 1, pos[1] - 1)] = "#"
            map_.setdefault((pos[0] - 1, pos[1] + 0), "?")
        elif d == "S":
            pos = (pos[0] + 2, pos[1])
            dist += 1
            map_[pos] = min(map_.get(pos, dist), dist)
            map_[(pos[0] - 1, pos[1])] = "-"
            map_.setdefault((pos[0] + 0, pos[1] + 1), "?")
            map_[(pos[0] + 1, pos[1] + 1)] = "#"
            map_.setdefault((pos[0] + 1, pos[1] + 0), "?")
            map_[(pos[0] + 1, pos[1] - 1)] = "#"
            map_.setdefault((pos[0] + 0, pos[1] - 1), "?")
        elif d == "(":
            for route, i in routes(directions, i):
                _draw_map(route, map_, pos, dist)
        i += 1


def routes(str_, i):
    assert str_[i] == "("
    stack = []
    j = i + 1
    for k in range(i + 1, len(str_)):
        if str_[k] == "(":
            stack.append(True)
        elif str_[k] == ")":
            if stack:
                stack.pop()
            else:
                yield str_[j:k], k
                break
        elif str_[k] == "|" and not stack:
            yield str_[j:k], k
            j = k + 1


def display_map(map_):
    # y-left, x-down
    min_x = min(map(lambda k: k[0], map_.keys()))
    max_x = max(map(lambda k: k[0], map_.keys()))
    min_y = min(map(lambda k: k[1], map_.keys()))
    max_y = max(map(lambda k: k[1], map_.keys()))
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            c = map_.get((x, y), " ")
            if not isinstance(c, str):
                c = "."
            print(c, end="")
        print()


def draw_map(directions):
    directions = directions[1:-1]
    pos = (0, 0)
    map_ = {pos: 0}
    map_[(pos[0] - 1, pos[1] - 1)] = "#"
    map_[(pos[0] + 0, pos[1] - 1)] = "?"
    map_[(pos[0] + 1, pos[1] - 1)] = "#"
    map_[(pos[0] + 1, pos[1] + 0)] = "?"
    map_[(pos[0] + 1, pos[1] + 1)] = "#"
    map_[(pos[0] + 0, pos[1] + 1)] = "?"
    map_[(pos[0] - 1, pos[1] + 1)] = "#"
    map_[(pos[0] - 1, pos[1] + 0)] = "?"
    _draw_map(directions, map_, pos)
    for pos in map_:
        if map_[pos] == "?":
            map_[pos] = "#"
    return map_


def main():
    directions = "^ENWWW(NEEE|SSE(EE|N))$"
    directions = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
    directions = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
    directions = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
    directions = read_directions("input")
    map_ = draw_map(directions)
    display_map(map_)
    result = max(map(lambda v: 0 if isinstance(v, str) else v, map_.values()))
    print(result)


if __name__ == "__main__":
    main()
