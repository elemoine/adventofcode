import math
from collections import Counter


def read_ratings(inputfile):
    with open(inputfile) as f:
        return [int(line) for line in f]


def count_contiguous(differences):
    cnt = Counter()
    c = 0
    for d in differences:
        if d == 1:
            c += 1
        elif c != 0:
            cnt[c] += 1
            c = 0
    return cnt


def count_cases(n):
    if n in (1, 2):
        return n
    return int(
        1
        + (n - 1)
        + math.factorial(n - 1) / (math.factorial(2) * math.factorial(n - 1 - 2))
    )


def main():
    ratings = read_ratings("input")
    ratings.append(0)
    ratings.sort()
    ratings.append(ratings[-1] + 3)
    differences = [ratings[i] - ratings[i - 1] for i in range(1, len(ratings))]
    c = count_contiguous(differences)
    result = math.prod(count_cases(n) ** c[n] for n in c)
    print(result)


if __name__ == "__main__":
    main()
