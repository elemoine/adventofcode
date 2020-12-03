from part1 import displayarea, readarea, counttrees


def main():
    area = readarea()
    displayarea(area)
    angles = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    prod = 1
    for angle in angles:
        ntrees = counttrees(area, angle=angle)
        print(f"Crossed {ntrees:3} trees with angle {angle}!")
        prod *= ntrees
    print(f"product = {prod}")


if __name__ == "__main__":
    main()
