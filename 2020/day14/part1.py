import re


def parse_mask(mask_str):
    m1 = int(mask_str.replace("X", "0"), 2)
    m2 = int(mask_str.replace("X", "1"), 2)
    return (m1, m2)


def apply_mask(val, mask):
    return (val | mask[0]) & mask[1]


def main(inputfile):
    mask = None
    memory = {}

    with open(inputfile) as f:
        instructions = [line.strip() for line in f]

    for instr in instructions:
        if match := re.match(r"^mask = ([X01]+)$", instr):
            mask = parse_mask(match.group(1))
        elif match := re.match(r"^mem\[(\d+)\] = (\d+)$", instr):
            assert mask
            memory[int(match.group(1))] = apply_mask(int(match.group(2)), mask)

    result = sum(memory.values())
    print(result)


if __name__ == "__main__":
    main("input")
