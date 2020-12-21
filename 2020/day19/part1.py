import itertools


def parse_rules(inputfile):
    with open(inputfile) as f:
        rules_, messages = f.read().split("\n\n")
    rules = {}
    for rule in rules_.splitlines():
        n, r = rule.split(":")
        r = r.strip()
        if r in ('"a"', '"b"'):
            rules[n] = r[1:-1]
        else:
            rules[n] = tuple(tuple(part.strip().split()) for part in r.split("|"))
    messages = [m.strip() for m in messages.splitlines()]
    return rules, messages


def possible_messages(n, rules, cache={}):
    v = rules[n]
    if isinstance(v, str):
        yield v
    else:
        for g in v:
            if g not in cache:
                p = itertools.product(
                    *map(lambda e: possible_messages(e, rules, cache), g)
                )
                cache[g] = tuple(p)
            yield from cache[g]


def tostr(s, cache={}):
    if s not in cache:
        cache[s] = "".join(e if isinstance(e, str) else tostr(e, cache) for e in s)
    return cache[s]


def main():
    received_rules, received_messages = parse_rules("input")
    messages = set(map(tostr, possible_messages("0", received_rules)))
    print(sum(int(m in messages) for m in received_messages))


if __name__ == "__main__":
    main()
