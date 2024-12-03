import re

token_spec = [
    ("mul", r"mul\((\d{1,3}),(\d{1,3})\)"),
    ("do", r"do\(\)"),
    ("dont", r"don't\(\)"),
]

token_regex = "|".join("(?P<%s>%s)" % pair for pair in token_spec)


r = 0

with open("input") as f_:
    enabled = True
    for line in f_:
        for m in re.finditer(token_regex, line):
            kind = m.lastgroup
            match kind:
                case "do":
                    enabled = True
                case "dont":
                    enabled = False
                case "mul":
                    if enabled:
                        a = int(m.group(2))
                        b = int(m.group(3))
                        r += a * b

print(r)
