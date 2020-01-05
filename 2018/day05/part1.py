def readinput():
    with open("input") as f:
        i = f.read().strip()
    return list(i)


def combined(a, b):
    return a.lower() == b.lower() and a != b


def processonce(polymer, length):
    i = 0  # current pointer
    j = 0  # insertion pointer
    while i < length:
        if i < length - 1 and combined(polymer[i], polymer[i + 1]):
            i += 2
        else:
            polymer[j] = polymer[i]
            j += 1
            i += 1
    return polymer, j


def process(polymer):
    length = len(polymer)
    while True:
        polymer, length_ = processonce(polymer, length)
        if length_ == length:
            return polymer[:length]
        length = length_


def main():
    polymer = list("dabAcCaCBAcCcaDA")
    polymer = process(polymer)
    assert "".join(polymer) == "dabCBAcaDA"

    polymer = readinput()
    polymer = process(polymer)
    print(len(polymer))


if __name__ == "__main__":
    main()
