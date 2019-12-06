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


def orbits(objects, obj):
    assert obj in objects
    if objects[obj] is None:
        return []
    return [objects[obj]] + orbits(objects, objects[obj])


def numorbits(objects, src, dst):
    assert src in objects
    assert dst in objects
    srcorbits = orbits(objects, src)
    dstorbits = orbits(objects, dst)
    commonobjects = set(srcorbits) & set(dstorbits)
    for o in dstorbits:
        if o in commonobjects:
            break
    else:
        raise Error()
    firstcommonobject = o
    # just a check
    for o in srcorbits:
        if o in commonobjects:
            break
    else:
        raise Error()
    assert o == firstcommonobject
    print("first common object", o)
    return srcorbits.index(firstcommonobject) + dstorbits.index(firstcommonobject)

if __name__ == "__main__":
    objects = objectsfromfile("testinput")
    objects["YOU"] = "K"
    objects["SAN"] = "I"
    result = numorbits(objects, "YOU", "SAN")
    assert result == 4

    objects = objectsfromfile("input")
    result = numorbits(objects, "YOU", "SAN")
    print(result)
