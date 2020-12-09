def is_valid(n, numbers, psize):
    b = [0] * numbers[n]
    for i in range(n - psize, n):
        if numbers[i] < len(b):
            b[numbers[i]] = 1
    for i in range(n - psize, n):
        j = numbers[n] - numbers[i]
        if j != numbers[i] and j >= 0 and b[j]:
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
