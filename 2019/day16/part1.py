import itertools

def _pattern(n, base):
    for e in itertools.cycle(base):
        for _ in range(n):
            yield e


def pattern(n, base=(0, 1, 0, -1)):
    g = _pattern(n, base)
    e = next(g)
    assert e == 0
    yield from g


def compute(numbers):
    output = []
    for i in range(1, len(numbers) + 1):
        s = sum(a * b for a, b in zip(numbers, pattern(i)))
        output.append(int(str(s)[-1]))
    return output


def fft(numbers, phases, expected=None):
    numbers = list(numbers)
    numbers = list(map(int, numbers))
    for _ in range(phases):
        numbers = compute(numbers)
    result = "".join(map(str, numbers[:8]))
    if expected:
        assert result == expected
    return result


if __name__ == "__main__":
    fft("12345678", 4, expected="01029498")
    fft("80871224585914546619083218645595", 100, "24176176")
    fft("19617804207202209144916044189917", 100, "73745418")
    fft("69317163492948606335995924319873", 100, "52432133")
    with open("input") as f:
        numbers = f.read().strip()
    print(fft(numbers, 100))
