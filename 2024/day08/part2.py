import itertools
from collections import defaultdict
from fractions import Fraction


def read_input():
    with open("input") as f_:
        rows = [row.strip() for row in f_]
    antennas = defaultdict(list)
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            c = rows[y][x]
            if c != ".":
                antennas[c].append((y, x))
    return antennas, (len(rows) - 1, len(rows[0]) - 1)


def within_bounds(pos, max_y, max_x):
    return pos[0] >= 0 and pos[0] <= max_y and pos[1] >= 0 and pos[1] <= max_x


def antinodes_for_positions(pos1, pos2, bounds):
    max_y, max_x = bounds

    dy = pos2[0] - pos1[0]
    dx = pos2[1] - pos1[1]

    a = Fraction(dx, dy)
    dx = a.numerator
    dy = a.denominator

    r = set()

    cur = pos1
    while within_bounds(cur, max_y, max_x):
        r.add(cur)
        cur = (cur[0] + dy, cur[1] + dx)

    cur = pos1
    while within_bounds(cur, max_y, max_x):
        r.add(cur)
        cur = (cur[0] - dy, cur[1] - dx)

    assert pos2 in r

    return r


def main():
    antennas, bounds = read_input()

    antinodes = set()
    for positions in antennas.values():
        for pos in itertools.combinations(positions, 2):
            pos1, pos2 = tuple(pos)
            antinodes |= antinodes_for_positions(pos1, pos2, bounds)

    print(len(antinodes))


if __name__ == "__main__":
    main()
