def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplify(n, d):
    cd = gcd(abs(n), abs(d))
    n, d = n / cd, d / cd
    return n, d


def setup(inputfile):
    with open(inputfile) as f:
        grid = [list(l.strip()) for l in f]
    return grid


def numasteroids(grid, yy, xx):
     detected = set()
     for y in range(len(grid)):
         for x in range(len(grid[y])):
             if (y == yy and x == xx) or grid[y][x] != "#":
                 continue
             detected.add(simplify(x - xx, y - yy))
     return len(detected)


def selectbest(grid):
    num, best = float("-inf"), None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                n = numasteroids(grid, y, x)
                if n > num:
                    best = (y, x)
                    num = n
    return best, num


if __name__ == "__main__":
    grid = setup("testinput")
    best, num = selectbest(grid)
    assert best == (4, 3)
    assert num == 8

    grid = setup("testinput1")
    best, num = selectbest(grid)
    assert best == (8, 5)
    assert num == 33

    grid = setup("testinput2")
    best, num = selectbest(grid)
    assert best == (13, 11)
    assert num == 210

    grid = setup("input")
    best, num = selectbest(grid)
    print(best, num)
