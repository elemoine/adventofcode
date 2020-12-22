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


def _possible_messages(n, rules, cache={}):
    v = rules[n]
    if isinstance(v, str):
        yield v
    else:
        for g in v:
            if g not in cache:
                p = itertools.product(
                    *map(lambda e: _possible_messages(e, rules, cache), g)
                )
                cache[g] = tuple(p)
            yield from cache[g]


def tostr(s, cache={}):
    if s not in cache:
        cache[s] = "".join(e if isinstance(e, str) else tostr(e, cache) for e in s)
    return cache[s]


def possible_messages(n, rules):
    return set(map(tostr, _possible_messages(n, rules)))


def is_valid(message, messages):
    for m in messages:
        if message.startswith(m):
            a, b = is_valid(message[len(m):], messages)
            return 1 + a, len(m) + b
    return 0, 0


def main():
    received_rules, received_messages = parse_rules("input")

    messages_rule0 = possible_messages("0", received_rules)
    n_valid = sum(int(m in messages_rule0) for m in received_messages)

    messages_rule42 = possible_messages("42", received_rules)
    messages_rule31 = possible_messages("31", received_rules)

    invalid_messages = set(m for m in received_messages if m not in messages_rule0)

    n_add_valid = 0
    for message in invalid_messages:
        cnt1, len1 = is_valid(message, messages_rule42)
        if cnt1 > 1:
            cnt2, len2 = is_valid(message[len1:], messages_rule31)
            if cnt1 > cnt2 > 0 and len1 + len2 == len(message):
                n_add_valid += 1

    print(n_valid + n_add_valid)


if __name__ == "__main__":
    main()
