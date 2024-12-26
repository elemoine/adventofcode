from collections import Counter


with open("input") as f_:
    secrets = [int(row.strip()) for row in f_]


def nextsecret(s):
    s = ((s * 64) ^ s) % 16777216
    s = ((s // 32) ^ s) % 16777216
    s = ((s * 2048) ^ s) % 16777216
    return s


def onedigit(s):
    return s % 10


scores = Counter()

track = {i: {"s": s, "p": None, "w": [], "v": set()} for i, s in enumerate(secrets)}

for _ in range(2000):
    for i in range(len(secrets)):
        t = track[i]

        s = nextsecret(t["s"])
        o = onedigit(s)

        if t["p"] is not None:
            t["w"].append(o - t["p"])
        if len(t["w"]) == 5:
            t["w"].pop(0)
            v = tuple(t["w"])
            assert len(v) == 4
            if v not in t["v"]:
                scores[v] += o
            t["v"].add(v)
        t["s"] = s
        t["p"] = o

print(scores.most_common(1)[0][1])
