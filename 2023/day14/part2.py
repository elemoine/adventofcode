with open("testinput") as f_:
    plateform = [list(row.strip()) for row in f_]


def display(plateform):
    for y in range(len(plateform)):
        for x in range(len(plateform[y])):
            print(plateform[y][x], end="")
        print()
    print()


def tilt_north(plateform):
    plateform_ = [r.copy() for r in plateform]
    for y in range(len(plateform_)):
        for x in range(len(plateform_[y])):
            if plateform_[y][x] != "O":
                continue
            yy = y
            while yy - 1 >= 0 and plateform_[yy - 1][x] == ".":
                plateform_[yy][x] = "."
                plateform_[yy - 1][x] = "O"
                yy -= 1
    return plateform_


def tilt_south(plateform):
    plateform_ = [r.copy() for r in plateform]
    for y in range(len(plateform_) - 1, -1, -1):
        for x in range(len(plateform_[y])):
            if plateform_[y][x] != "O":
                continue
            yy = y
            while yy + 1 < len(plateform_) and plateform_[yy + 1][x] == ".":
                plateform_[yy][x] = "."
                plateform_[yy + 1][x] = "O"
                yy += 1
    return plateform_


def tilt_west(plateform):
    plateform_ = list(map(list, zip(*plateform)))
    plateform_ = tilt_north(plateform_)
    return list(map(list, zip(*plateform_)))


def tilt_east(plateform):
    plateform_ = list(map(list, zip(*plateform)))
    plateform_ = tilt_south(plateform_)
    return list(map(list, zip(*plateform_)))


def load(plateform):
    return sum(
        len(plateform) - y
        for y in range(len(plateform))
        for x in range(len(plateform[y]))
        if plateform[y][x] == "O"
    )

N = 1000000000

for i in range(N):
    for tilt in (tilt_north, tilt_west, tilt_south, tilt_east):
        plateform = tilt(plateform)
    l_ = load(plateform)


# with testinput
# 69239 69  69239 % 7 = 2
# 69240 69
# 69241 65
# 69242 64
# 69243 65  1000000000 % 7 = 6
# 69244 63
# 69245 68


# with input
# 8749 99862  8749 % 28 = 13
# 8750 99862
# 8751 99855
# 8752 99849
# 8753 99854
# 8754 99862
# 8755 99875
# 8756 99867  8756 % 28 = 20  1000000000 % 28 = 20
# 8757 99854
# 8758 99856
# 8759 99851
# 8760 99859
# 8761 99854
# 8762 99876
# 8763 99869
# 8764 99859
# 8765 99848
# 8766 99852
# 8767 99861
# 8768 99859
# 8769 99868
# 8770 99870
# 8771 99861
# 8772 99853
# 8773 99844
# 8774 99862
# 8775 99861
# 8776 99873
