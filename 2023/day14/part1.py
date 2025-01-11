with open("input") as f_:
    plateform = [list(row.strip()) for row in f_]


def display():
    for y in range(len(plateform)):
        for x in range(len(plateform[y])):
            print(plateform[y][x], end="")
        print()
    print()


def tilt():
    for y in range(len(plateform)):
        for x in range(len(plateform[y])):
            if plateform[y][x] != "O":
                continue
            yy = y
            while yy - 1 >= 0 and plateform[yy - 1][x] == ".":
                plateform[yy][x] = "."
                plateform[yy - 1][x] = "O"
                yy -= 1


tilt()

r = sum(
    len(plateform) - y
    for y in range(len(plateform))
    for x in range(len(plateform[y]))
    if plateform[y][x] == "O"
)
print(r)
