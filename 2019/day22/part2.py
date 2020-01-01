#
# https://github.com/emilysmiddleton/advent-of-code-2019/blob/master/src/day22/day22.md
#


def readoperations(inputfile):
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


def deal(decklen, operations, i):
    for o, n in operations:
        if o == "cut":
            if n >= 0:
                if i >= n:
                    i -= n
                else:
                    i += decklen - n
            else:
                if i < decklen + n:
                    i -= n
                else:
                    i -= decklen + n
        elif o == "dealintonewstack":
            i = decklen - 1 - i
        elif o == "dealwithincrement":
            i = (i * n) % decklen
        else:
            raise ValueError("unknown operation", o)
    return i


def combineoperations(decklen, operations):
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


def main(inputfile):
    operations = readoperations(inputfile)
    a, b = combineoperations(10007, operations)
    print(a, b, (a * 2019 + b) % 10007)


if __name__ == "__main__":
    main("input")
