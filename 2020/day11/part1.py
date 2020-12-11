def readgrid(inputfile):
    with open(inputfile) as f:
        return [list(line.strip()) for line in f]


def displaygrid(grid):
    for r in grid:
        for c in r:
            print(c, end="")
        print("\n", end="")
    print()


def seatsaroundme(grid, i, j):
    assert grid[i][j] in ("L", "#")
    if i > 0:
        if j > 0:
            if grid[i - 1][j - 1] != ".":
                yield (i - 1, j - 1)
        if grid[i - 1][j] != ".":
            yield (i - 1, j)
        if j < len(grid[i]) - 1:
            if grid[i - 1][j + 1] != ".":
                yield (i - 1, j + 1)
    if j > 0:
        if grid[i][j - 1] != ".":
            yield (i, j - 1)
    if j < len(grid[i]) - 1:
        if grid[i][j + 1] != ".":
            yield (i, j + 1)
    if i < len(grid) - 1:
        if j > 0:
            if grid[i + 1][j - 1] != ".":
                yield (i + 1, j - 1)
        if grid[i + 1][j] != ".":
            yield (i + 1, j)
        if j < len(grid[i]) - 1:
            if grid[i + 1][j + 1] != ".":
                yield (i + 1, j + 1)


def emptygrid(grid):
    newgrid = []
    for i in range(len(grid)):
        newgrid.append([])
        for j in range(len(grid[i])):
            newgrid[i].append(".")
    return newgrid


def gridsareequal(grid1, grid2):
    assert len(grid1) == len(grid2)
    for i in range(len(grid1)):
        assert len(grid1[i]) == len(grid2[i])
        for j in range(len(grid1[i])):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True


def countoccupied(grid):
    return sum(int(c == "#") for r in grid for c in r)


def changestate(grid):
    newgrid = emptygrid(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == "L":
                if all(grid[r][c] == "L" for r, c in seatsaroundme(grid, i, j)):
                    newgrid[i][j] = "#"
                else:
                    newgrid[i][j] = grid[i][j]
            else:
                if (
                    sum(int(grid[r][c] == "#") for r, c in seatsaroundme(grid, i, j))
                    >= 4
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
