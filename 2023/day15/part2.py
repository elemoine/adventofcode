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


boxes = {}

for s in steps:
    if "-" in s:
        label, _ = s.split("-")
        box = hash(label)
        if box in boxes:
            if label in boxes[box][1]:
                del boxes[box][1][label]
                boxes[box][0].remove(label)
    else:
        assert "=" in s
        label, focal = s.split("=")
        focal = int(focal)
        box = hash(label)
        if box not in boxes:
            boxes[box] = ([label], {label: focal})
        else:
            boxes[box][1][label] = focal
            if label not in boxes[box][0]:
                boxes[box][0].append(label)


r = 0
for box in boxes:
    for s, label in enumerate(boxes[box][0]): 
        r += (box + 1) * (s + 1) * boxes[box][1][label]
print(r)
