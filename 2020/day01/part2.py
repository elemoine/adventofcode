from part1 import twosum


def threesum(numbers, target):
    for i in range(len(numbers)):
        a, b = twosum(numbers[i + 1:], target - numbers[i])
        if a is not None:
            return numbers[i], a, b
    return None, None, None


def main(target):
    with open("input") as f:
        numbers = [int(row.strip()) for row in f]
    numbers.sort()
    a, b, c = threesum(numbers, target)
    if a is None:
        return "No result"
    return a * b * c


if __name__ == "__main__":
    print(main(2020))
