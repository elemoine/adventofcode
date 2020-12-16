import math
from collections import defaultdict

from part1 import is_valid, parse_notes


def valid_tickets(nearby_tickets, rules):
    for ticket in nearby_tickets:
        for value in ticket:
            valid = any(is_valid(value, rule) for rule in rules.values())
            if not valid:
                break
        else:
            yield ticket


def main():
    rules, my_ticket, nearby_tickets = parse_notes("input")

    # filter out invalid nearby tickets
    nearby_tickets = valid_tickets(nearby_tickets, rules)

    # determine all the possible rules for each field
    d = defaultdict(set)
    for field, values in enumerate(zip(*nearby_tickets)):
        for rule_name, rule in rules.items():
            v = all(is_valid(value, rule) for value in values)
            if v:
                d[field].add(rule_name)

    # narrow it down to one rule per field
    found = set()
    while sum(len(names) for names in d.values()) != len(d):
        for field, rule_names in d.items():
            assert len(rule_names) > 0
            if len(rule_names) == 1:
                found |= rule_names
            else:
                d[field] = rule_names - found

    # compute the final result
    d = {field: list(rule_names)[0] for field, rule_names in d.items()}
    result = math.prod(
        my_ticket[field]
        for field in range(len(my_ticket))
        if d[field].startswith("departure")
    )
    print(result)


if __name__ == "__main__":
    main()
