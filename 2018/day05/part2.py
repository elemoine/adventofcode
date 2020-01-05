import string


def readinput():
    with open("input") as f:
        i = f.read().strip()
    return list(i)


def combined(a, b):
    return a.lower() == b.lower() and a != b


def processonce(polymer, length, unit):
    i = 0  # current pointer
    j = 0  # insertion pointer
    while i < length:
        if polymer[i].lower() == unit:
            i += 1
        elif i == length - 1 or not combined(polymer[i], polymer[i + 1]):
            polymer[j] = polymer[i]
            j += 1
            i += 1
        else:
            i += 2
    return polymer, j


def process(polymer, unit):
    length = len(polymer)
    while True:
        polymer, length_ = processonce(polymer, length, unit)
        if length_ == length:
            return polymer[:length]
        length = length_


def main():
    polymer = readinput()
    best = float("+inf")
    for unit in string.ascii_lowercase:
        newpolymer = process(polymer.copy(), unit)
        if len(newpolymer) < best:
            best = len(newpolymer)
            print(unit, best)
    print(best)


if __name__ == "__main__":
    main()
