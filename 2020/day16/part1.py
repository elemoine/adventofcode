import re


def parse_rule(rule_str):
    m = re.match(r"^([\w\s]+):\s+(\d+)-(\d+)\s+or\s+(\d+)-(\d+)$", rule_str)
    return {
        m.group(1): (
            (int(m.group(2)), int(m.group(3))),
            (int(m.group(4)), int(m.group(5))),
        )
    }


def parse_ticket(ticket_str):
    return tuple(int(n) for n in ticket_str.split(","))


def parse_notes(inputfile):
    rules, my_ticket, nearby_tickets = {}, None, []
    with open(inputfile) as f:
        section = 0
        for line in f:
            line = line.strip()
            if line != "":
                if section == 0:
                    rules.update(parse_rule(line))
                elif section == 1 and line != "your ticket:":
                    my_ticket = parse_ticket(line)
                elif section == 2 and line != "nearby tickets:":
                    nearby_tickets.append(parse_ticket(line))
            else:
                section += 1
    return rules, my_ticket, tuple(nearby_tickets)


def is_valid(value, rule):
    return any(interval[0] <= value <= interval[1] for interval in rule)


def invalid_values(nearby_tickets, rules):
    for ticket in nearby_tickets:
        for value in ticket:
            valid = any(is_valid(value, rule) for rule in rules.values())
            if not valid:
                yield value


def main():
    rules, my_ticket, nearby_tickets = parse_notes("input")
    ticket_scaning_error_rate = sum(invalid_values(nearby_tickets, rules))
    print(ticket_scaning_error_rate)


if __name__ == "__main__":
    main()
