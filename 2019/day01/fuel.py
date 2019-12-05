import math


def fuel(mass):
    return math.floor(mass / 3) - 2


if __name__ == "__main__":
    with open("input") as f:
        total = 0
        for mass in f:
            r = fuel(int(mass))
            while r > 0:
                total += r
                r = fuel(r)
        print(total)
