def numorbits(objects, obj):
    assert obj in objects
    if objects[obj] is None:
        return 0
    return 1 + numorbits(objects, objects[obj])


def objectsfromfile(inputfile):
    objects = {} 
    with open(inputfile) as f:
        for l in f:
            obj1, obj2 = l.strip().split(")")
            assert obj2 not in objects or objects[obj2] is None
            if obj1 not in objects:
                objects[obj1] = None
            objects[obj2] = obj1
    return objects


def execute(inputfile):
    objects = objectsfromfile(inputfile)
    return sum(numorbits(objects, obj) for obj in objects)


if __name__ == "__main__":
    result = execute("testinput")
    assert result == 42

    result = execute("input")
    print(result)
