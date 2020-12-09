from part1 import find_first_invalid, read_numbers


def sumto(target, numbers):
    for psize in range(2, len(numbers)):
        for i in range(0, len(numbers) - psize + 1):
            p = numbers[i:i + psize]
            if target == sum(p):
                return p
    raise Exception("oops")


def main():
    numbers = read_numbers("input")
    invalid = find_first_invalid(numbers, 25)
    partition = sumto(invalid, numbers)
    print(max(partition) + min(partition))


if __name__ == "__main__":
    main()
