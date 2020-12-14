import itertools
import re


def x_values(mask_str):
    """
    Return an iterator providing all the X values combinations for the
    given mask. The iterator yields values of the form ((7, 0), (8, 1)).
    """
    m = list(mask_str)
    x_pos = [pos for pos, bit in enumerate(m) if bit == "X"]
    bits = itertools.product("01", repeat=len(x_pos))
    return (zip(x_pos, b) for b in bits)


def write_to_mem(memory, location, value, mask):
    """
    Write a value to a given memory location.
    """
    mask_int = int(mask.replace("X", "0"), 2)
    location = location | mask_int
    location = list("{0:036b}".format(location))
    for xv in x_values(mask):
        for bit_pos, bit_val in xv:
            location[bit_pos] = bit_val
        memory[int("".join(location), 2)] = value


def main(inputfile):
    mask = None
    memory = {}

    with open(inputfile) as f:
        instructions = [line.strip() for line in f]

    for instr in instructions:
        if match := re.match(r"^mask = ([X01]+)$", instr):
            mask = match.group(1)
        elif match := re.match(r"^mem\[(\d+)\] = (\d+)$", instr):
            location, value = int(match.group(1)), int(match.group(2))
            write_to_mem(memory, location, value, mask)

    result = sum(memory.values())
    print(result)


if __name__ == "__main__":
    main("input")
