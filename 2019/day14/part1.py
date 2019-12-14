import math
from collections import defaultdict


def readreactions(inputfile):
    reactions = {}
    with open(inputfile) as f:
        lines = [l.strip() for l in f]
    for line in lines:
        line = line.split(",")
        line = list(map(str.strip, line))
        tmp = list(map(str.strip, line[-1].split("=>")))
        assert len(tmp) == 2
        input, output = tmp
        input = input.split(" ")
        inputs = [(int(input[0]), input[1])]
        for e in line[-2::-1]:
            quantity, chemical = e.split(" ")
            inputs.append((int(quantity), chemical))
        outputquantity, outputchemical = output.split(" ")
        reactions[outputchemical] = (int(outputquantity), tuple(inputs))
    return reactions


def quantityore(chemical, quantity, reactions, extra):
    assert quantity >= 0
    if chemical == "ORE" or quantity == 0:
        return quantity
    assert chemical in reactions
    quant, chemicals = reactions[chemical]
    mult = math.ceil(quantity / quant)
    ore = 0
    for c in chemicals:
        q = min(extra[c[1]], c[0] * mult)
        extra[c[1]] -= q
        ore += quantityore(c[1], c[0] * mult - q, reactions, extra)
    extra[chemical] += mult * quant - quantity
    assert extra[chemical] >= 0
    return ore


if __name__ == "__main__":
    reactions = readreactions("input")
    extra = defaultdict(int)
    ore = quantityore("FUEL", 1, reactions, extra)
    print(ore)
