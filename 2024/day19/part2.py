with open("input") as f_:
    rows = [row.strip() for row in f_]

patterns = set(pattern.strip() for pattern in rows[0].split(","))
designs = [row.strip() for row in rows[2:]]


def number_of_arrangements(design, cache={}):
    if design in cache:
        return cache[design]
    cnt = 0
    if len(design) == 0:
        pass
    elif len(design) == 1:
        cnt = int(design in patterns)
    else:
        if design in patterns:
            cnt = 1
        for i in range(1, len(design)):
            if design[:i] not in patterns:
                continue
            cnt += number_of_arrangements(design[i:], cache)
    cache[design] = cnt
    return cnt


# print(number_of_arrangements("gbbr"))
# print(number_of_arrangements("rrbgbr"))


r = sum(number_of_arrangements(design) for design in designs)
print(r)
