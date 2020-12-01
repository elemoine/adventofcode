def twosum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        v = numbers[left] + numbers[right]
        if v == target:
            return numbers[left], numbers[right]
        if v < target:
            left += 1
        else:
            right -= 1
    return None, None


def main(target):
    with open("input") as f:
        numbers = [int(row.strip()) for row in f]
    numbers.sort()
    a, b = twosum(numbers, target)
    if a is None:
        return "No result"
    return a * b


if __name__ == "__main__":
    print(main(2020))
