from collections import Counter


def parserow(row):
    policy, password = tuple(map(str.strip, row.split(":")))
    spec, char = policy.split()
    spec1, spec2 = tuple(map(int, spec.split("-")))
    return spec1, spec2, char, password


def main():
    with open("input") as f:
        rows = [row.strip() for row in f]
    num_valid = 0
    for row in rows:
        min_, max_, char, password = parserow(row)
        counter = Counter(password)
        if counter[char] >= min_ and counter[char] <= max_:
            num_valid += 1
    print(num_valid)


if __name__ == "__main__":
    main()
