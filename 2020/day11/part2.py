from part1 import countoccupied, emptygrid, gridsareequal, readgrid


def seatsinsight(grid, i, j):
    directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
    for d in directions:
        r = i + d[0]
        c = j + d[1]
        while 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            if grid[r][c] != ".":
                yield r, c
                break
            r += d[0]
            c += d[1]


def changestate(grid):
    newgrid = emptygrid(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == "L":
                if all(grid[r][c] == "L" for r, c in seatsinsight(grid, i, j)):
                    newgrid[i][j] = "#"
                else:
                    newgrid[i][j] = grid[i][j]
            else:
                if (
                    sum(int(grid[r][c] == "#") for r, c in seatsinsight(grid, i, j))
                    >= 5
                ):
                    newgrid[i][j] = "L"
                else:
                    newgrid[i][j] = grid[i][j]
    return newgrid


def play(grid):
    while not gridsareequal(grid, newgrid := changestate(grid)):
        grid = newgrid
    return newgrid


def main():
    grid = play(readgrid("input"))
    print(countoccupied(grid))


if __name__ == "__main__":
    main()
