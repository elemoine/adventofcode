from part1 import parserow


def main():
    with open("input") as f:
        rows = [row.strip() for row in f]
    num_valid = 0
    for row in rows:
        pos1, pos2, char, password = parserow(row)
        pos1 -= 1
        pos2 -= 1
        if (password[pos1] == char and password[pos2] != char) or (
            password[pos1] != char and password[pos2] == char
        ):
            num_valid += 1
    print(num_valid)


if __name__ == "__main__":
    main()
