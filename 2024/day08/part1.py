from collections import defaultdict
import itertools


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

    antinode1 = (pos1[0] - dy, pos1[1] - dx)
    antinode2 = (pos2[0] + dy, pos2[1] + dx)

    r = set()

    if within_bounds(antinode1, max_y, max_x):
        r.add(antinode1)

    if within_bounds(antinode2, max_y, max_x):
        r.add(antinode2)

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
