with open("input") as f_:
    lines = f_.readlines()

list1, list2 = zip(*[line.strip().split() for line in lines])

list1 = sorted([int(e) for e in list1])
list2 = sorted([int(e) for e in list2])

assert len(list1) == len(list2)

result = sum(abs(list1[i] - list2[i]) for i in range(len(list1)))
print(result)
