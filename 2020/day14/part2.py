import itertools
import re


def x_vals(mask_str):
    m = list(mask_str)
    x_pos = [pos for pos, bit in enumerate(m) if bit == "X"]
    iterables = (itertools.product((p,), ("0", "1")) for p in x_pos)
    return itertools.product(*iterables)


def write(memory, location, value, mask):
    location = list("{0:036b}".format(location))
    for p in x_vals(mask):
        loc = list(location)
        for pos, val in p:
            loc[pos] = val
        loc = int("".join(loc), 2)
        loc = loc | int(mask.replace("X", "0"), 2)
        memory[loc] = value


def main(inputfile):
    mask = None
    memory = {}

    with open(inputfile) as f:
        instructions = [line.strip() for line in f]

    for instr in instructions:
        if match := re.match(r"^mask = ([X01]+)$", instr):
            mask = match.group(1)
        elif match := re.match(r"^mem\[(\d+)\] = (\d+)$", instr):
            location = int(match.group(1))
            value = int(match.group(2))
            write(memory, location, value, mask)

    result = sum(memory.values())
    print(result)


if __name__ == "__main__":
    main("input")
