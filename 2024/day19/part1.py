with open("input") as f_:
    rows = [row.strip() for row in f_]

patterns = set(pattern.strip() for pattern in rows[0].split(","))
designs = [row.strip() for row in rows[2:]]


def is_possible(design, cache={}):
    if design in cache:
        return cache[design]
    if not design or design in patterns:
        r = True
    else:
        r = any(
            is_possible(design[:i], cache) and is_possible(design[i:], cache)
            for i in range(1, len(design))
        )
    cache[design] = r
    return r


r = sum(is_possible(design) for design in designs)
print(r)
