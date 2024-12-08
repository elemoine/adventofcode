import itertools
from operator import add, mul


def operators(n):
    yield from itertools.product([add, mul], repeat=n)


def compute(numbers, operators):
    i = 0
    r = numbers[i]
    for op in operators:
        i += 1
        r = op(r, numbers[i])
    return r


def test(numbers, result):
    return any(compute(numbers, ops) == result for ops in operators(len(numbers) - 1))


def read_equations(rows):
    equations = []
    for row in rows:
        result, numbers = row.split(":")
        numbers = tuple(map(lambda n: int(n.strip()), numbers.strip().split(" ")))
        equations.append((numbers, int(result)))
    return equations


def main():
    with open("input") as f_:
        rows = [row.strip() for row in f_]
    equations = read_equations(rows)

    r = sum(equation[1] for equation in equations if test(equation[0], equation[1]))
    print(r)


if __name__ == "__main__":
    main()
