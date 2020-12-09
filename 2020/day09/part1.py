def is_valid(n, numbers, psize):
    for i in range(n - psize, n):
        ni = numbers[i]
        for j in range(i + 1, n):
            nj = numbers[j]
            if ni != nj and ni + nj == numbers[n]:
                return True
    return False


def find_first_invalid(numbers, psize):
    for i in range(psize, len(numbers)):
        if not is_valid(i, numbers, psize):
            return numbers[i]


def read_numbers(inputfile):
    with open(inputfile) as f:
        return [int(line) for line in f]


def main():
    numbers = read_numbers("input")
    invalid = find_first_invalid(numbers, 25)
    print(invalid)


if __name__ == "__main__":
    main()
