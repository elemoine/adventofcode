from collections import Counter


with open("input") as f_:
    lines = f_.readlines()

list1, list2 = zip(*[line.strip().split() for line in lines])

list1 = [int(e) for e in list1]
list2 = Counter([int(e) for e in list2])

result = sum(entry * list2[entry] for entry in list1)
print(result)
