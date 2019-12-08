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
    layerwithfewer0digits, numzerosmin = None, float("inf")
    for layer in layers:
        counter = collections.Counter(layer)
        numzeros = counter[0]
        if numzeros < numzerosmin:
            numzerosmin = numzeros
            layerwithfewer0digits = counter
    assert layerwithfewer0digits is not None
    result = layerwithfewer0digits[1] * layerwithfewer0digits[2]
    print(result)
