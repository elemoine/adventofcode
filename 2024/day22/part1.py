with open("input") as f_:
    secrets = [int(row.strip()) for row in f_]

r = 0
for s in secrets:
    for _ in range(2000):
        s = ((s * 64) ^ s) % 16777216
        s = ((s // 32) ^ s) % 16777216
        s = ((s * 2048) ^ s) % 16777216
    r += s
print(r)
