def hash_(v, c):
    return ((v + ord(c)) * 17) % 256


def hash(s):
    v = 0
    for c in s:
        v = hash_(v, c)
    return v


with open("input") as f_:
    steps = []
    for row in f_:
        steps.extend(row.strip().split(","))


r = sum(hash(s) for s in steps)
print(r)
