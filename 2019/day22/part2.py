#
# https://github.com/emilysmiddleton/advent-of-code-2019/blob/master/src/day22/day22.md
#

import math


def read(inputfile):
    with open(inputfile) as f:
        operations = [l.strip() for l in f]
    for i in range(len(operations)):
        operation = operations[i].split(" ")
        try:
            n = int(operation[-1])
        except ValueError:
            n = None
        if n is not None:
            operation = ("".join(operation[:-1]), n)
        else:
            operation = ("".join(operation), -1)
        operations[i] = operation
    return operations


def combine(decklen, operations):
    # dealintonewstack (-1 - x) mod m
    # cut (x - n) mod m
    # dealwithincrement (x * n) mod m
    #
    # example: m = 10, x = 2
    # - cut 6 : 2 - 6 mod 10 = -4 mod 10 = 6
    # - deal with increment 7 = 6 * 7 mod 10 = 2
    # - deal into new stack : -1 - 2 mod 10 = 7
    #
    a, b = 1, 0
    for o, n in operations:
        if o == "dealintonewstack":
            # (-1 - x) = (-1 - (ax + b)) = -ax + (-b - 1)
            a = -a
            b = -b - 1
        elif o == "cut":
            # (x - n) = ((ax + b) - n) = ax + b - n
            b = b - n
        elif o == "dealwithincrement":
            # (x * n) = ((ax + b) * n) = n * a * x + n * b
            a = a * n
            b = b * n
        else:
            raise ValueError("unknown operation", o)
    return a % decklen, b % decklen


def repeat(a, b, m, n):
    # we need to repeat n times
    #
    # to repeat 2 times: a2, b2 = (a**2) % m, (b * (a + 1)) % m
    # to repeat 4 times: a4, b4 = (a2**2) % m, (b2 * (a2 + 1)) % m
    # to repeat 8 times: a8, b8 = (a4**2) % m, (b4 * (a4 + 1)) % m
    # ...
    # we repeat 2**logn times, 2**logn times what's left, etc.
    a1, b1 = 1, 0
    n2 = n
    while n2 > 0:
        a2, b2 = a, b
        logn = math.floor(math.log(n2, 2))
        for _ in range(logn):
            a2, b2 = (a2**2) % m, (b2 * (a2 + 1)) % m
        a1, b1 = (a1 * a2) % m, (a1 * b2 + b1) % m
        n2 -= 2**logn
    assert n2 == 0
    return a1, b1


def inverse(a, b):
    m = b
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a // b
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        a, b = b, a % b
    return prevx % m


def main(inputfile):
    m, x, n = 10007, 6326, 1
    operations = read(inputfile)
    a, b = combine(m, operations)
    a, b = repeat(a, b, m, n)
    i = inverse(a, m)
    print(((x - b) * i) % m)

    m, x, n = 119315717514047, 2020, 101741582076661
    operations = read(inputfile)
    a, b = combine(m, operations)
    a, b = repeat(a, b, m, n)
    i = inverse(a, m)
    print(((x - b) * i) % m)


if __name__ == "__main__":
    main("input")
