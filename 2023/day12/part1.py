def arrangements(sp, sz):
    if not sp:
        return 1 if not sz else 0
    if not sz:
        return 1 if "#" not in sp else 0
    if sp[0] == ".":
        return arrangements(sp[1:], sz)
    if sp[: sz[0]] == "#" * sz[0]:
        if sz[0] < len(sp) and sp[sz[0]] == "#":
            return 0
        return arrangements(sp[sz[0] + 1 :], sz[1:])
    a = 0
    if sz[0] <= len(sp) and "." not in sp[: sz[0]]:
        if sz[0] == len(sp) or sp[sz[0]] == ".":
            a = arrangements(sp[sz[0] :], sz[1:])
        elif sp[sz[0]] == "?":
            a = arrangements(sp[sz[0] + 1 :], sz[1:])
    if sp[0] == "?":
        a += arrangements(sp[1:], sz)
    return a


assert arrangements("", []) == 1
assert arrangements("", [1]) == 0
assert arrangements("...", []) == 1
assert arrangements("...", [1]) == 0
assert arrangements("#...", [1]) == 1
assert arrangements("#...", [2]) == 0
assert arrangements("##...", [2]) == 1
assert arrangements("#.#..", [2]) == 0
assert arrangements(".#.###.#.######", [1, 3, 1, 6]) == 1
assert arrangements("#....######..#####.", [1, 6, 5]) == 1
assert arrangements("?", [1]) == 1
assert arrangements("??", [2]) == 1
assert arrangements("??.", [2]) == 1
assert arrangements("??#", [2]) == 1
assert arrangements("??##", [2]) == 1
assert arrangements("??#.", [2]) == 1
assert arrangements("???.###", [1, 1, 3]) == 1
assert arrangements(".??..??...?##.", [1, 1, 3]) == 4
assert arrangements("?###????????", [3, 2, 1]) == 10

with open("input") as f_:
    springs = []
    for row in f_:
        sp, sz = row.strip().split(" ")
        sz = list(map(int, sz.split(",")))
        springs.append((sp, sz))


n = sum(arrangements(sp, sz) for sp, sz in springs)
print(n)
