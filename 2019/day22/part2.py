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


def main(inputfile):
    operations = readoperations(inputfile)
    i = deal(119315717514047, operations, 2020)
    print(i)


if __name__ == "__main__":
    main("input")
