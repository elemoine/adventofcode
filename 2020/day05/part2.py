from part1 import seatid


def main():
    with open("input") as f:
        seats = [l.strip() for l in f]
    seatids = list(sorted(seatid(s) for s in seats))
    for i in range(1, len(seatids)):
        if seatids[i] - seatids[i - 1] != 1:
            print(seatids[i - 1] + 1)
            break


if __name__ == "__main__":
    main()
