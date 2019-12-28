from collections import deque


def dealintonewstack(deck):
    return list(reversed(deck))


def cutncards(deck, n):
    return deck[n:] + deck[:n]


def dealwithincrement(deck, n):
    decklen = len(deck)
    newdeck = [-1] * decklen
    deck = deque(deck)
    i = 0
    while deck:
        assert newdeck[i] == -1
        newdeck[i] = deck.popleft()
        i = (i + n) % decklen
    return newdeck


def readsteps(inputfile):
    with open(inputfile) as f:
        steps = [l.strip() for l in f]
    for i in range(len(steps)):
        step = steps[i].split(" ")
        try:
            n = int(step[-1])
        except ValueError:
            n = None
        if n is not None:
            step = ("".join(step[:-1]), n)
        else:
            step = ("".join(step),)
        steps[i] = step
    return steps


def main(inputfile, deck, expected=None):
    steps = readsteps(inputfile)
    for step in steps:
        if step[0] == "dealwithincrement":
            deck = dealwithincrement(deck, step[1])
        elif step[0] == "dealintonewstack":
            deck = dealintonewstack(deck)
        elif step[0] == "cut":
            deck = cutncards(deck, step[1])
        else:
            raise ValueError("Unknown step")
    if expected:
        assert deck == expected
    return deck


if __name__ == "__main__":
    main("testinput0", list(range(10)), expected=[0, 3, 6, 9, 2, 5, 8, 1, 4, 7])
    main("testinput3", list(range(10)), expected=[9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
    deck = main("input", list(range(10007)))
    print(deck.index(2019))
