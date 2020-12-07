def num(s, c):
    b = [int(_c == c) for _c in s]
    return sum(2**i if v else 0 for i, v in enumerate(b[::-1]))


def seatid(s):
    return num(s[:7], "B") * 8 + num(s[7:], "R")


def main():
    with open("input") as f:
        seats = [l.strip() for l in f]
    print(max(seatid(seat) for seat in seats))


if __name__ == "__main__":
    main()
