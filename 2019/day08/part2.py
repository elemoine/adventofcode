import collections


if __name__ == "__main__":
    with open("input") as f:
        image = f.read().strip()
    image = list(map(int, image))
    layers = []
    start, stop = 0, 150
    while True:
        layer = image[start:stop]
        lenlayer = len(layer)
        if lenlayer == 150:
            layers.append(layer)
        elif lenlayer == 0:
            break
        else:
            raise Error()
        start += 150
        stop += 150
    result = []
    for row in range(6):
        result.append([])
        for col in range(25):
            for layer in layers:
                if layer[row * 25 + col] != 2:
                    result[row].append(layer[row * 25 + col])
                    break
            else:
                result[row].append(2)
    for row in range(6):
        for col in range(25):
            char = "*" if result[row][col] == 1 else " "
            print(char, end="")
        print("\n", end="")
