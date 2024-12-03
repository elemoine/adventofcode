import re

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

r = 0

with open("input") as f_:
    for line in f_:
        for m in pattern.finditer(line):
            a = int(m.group(1))
            b = int(m.group(2))
            r += a * b

print(r)
