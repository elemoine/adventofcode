import math


def message(inputfile):
    with open(inputfile) as f:
        numbers = f.read().strip()
    offset = int(numbers[:7])
    numbers = list(numbers)
    numbers = list(map(int, numbers))
    segment = math.ceil(offset / len(numbers))
    offset = segment * len(numbers) - offset
    numbers = numbers[-offset:] + numbers * (10000 - segment)
    for _ in range(100):
        sum_ = sum(numbers)
        prev = numbers[0]
        numbers[0] = int(str(sum_)[-1])
        for i in range(1, len(numbers)):
            s = sum_ - prev
            sum_ = s
            prev = numbers[i]
            numbers[i] = int(str(s)[-1])
    result = "".join(map(str, numbers[:8]))
    return result


if __name__ == "__main__":
    assert message("testinput0") == "84462026"
    assert message("testinput1") == "78725270"
    assert message("testinput2") == "53553731"
    print(message("input"))
