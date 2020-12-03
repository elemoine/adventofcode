def readarea():
    with open("input") as f:
        return tuple(row.strip() for row in f)


def displayarea(area):
    for row in area:
        for cell in row:
            print(cell, end="")
        print("\n", end="")


def counttrees(area, angle):
    width = len(area[0])
    ntrees = 0
    pos = [0, 0]
    while pos[0] < len(area):
        if area[pos[0]][pos[1]] == "#":
            ntrees += 1
        pos[0] += angle[0]
        pos[1] = (pos[1] + angle[1]) % width
    return ntrees


def main():
    area = readarea()
    displayarea(area)
    ntrees = counttrees(area, angle=(1, 3))
    print(f"Crossed {ntrees} trees!")


if __name__ == "__main__":
    main()
