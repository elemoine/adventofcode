from part1 import readpassports, requiredfields


def isvalidbyr(passport):
    return 1920 <= int(passport["byr"]) <= 2002


def isvalidiyr(passport):
    return 2010 <= int(passport["iyr"]) <= 2020


def isvalideyr(passport):
    return 2020 <= int(passport["eyr"]) <= 2030


def isvalidhgt(passport):
    hgt = passport["hgt"]
    if len(hgt) <= 2:
        return False
    hgtv, hgtu = int(hgt[:-2]), hgt[-2:]
    if hgtu not in ("cm", "in"):
        return False
    return (150 <= hgtv <= 193 and hgtu == "cm") or (59 <= hgtv <= 76 and hgtu == "in")


def isvalidhcl(passport):
    hcl = passport["hcl"]
    if len(hcl) != 7 or hcl[0] != "#":
        return False
    try:
        int(hcl[1:], 16)
    except ValueError:
        return False
    else:
        return True


def isvalidecl(passport):
    return passport["ecl"] in (
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    )


def isvalidpid(passport):
    pid = passport["pid"]
    if len(pid) != 9:
        return False
    try:
        int(pid)
    except ValueError:
        return False
    else:
        return True


def isvalid(passport):
    if not requiredfields <= set(passport.keys()):
        return False
    return all(globals()[f"isvalid{field}"](passport) for field in requiredfields)


def countvalidpassports(passports):
    return sum(int(isvalid(passport)) for passport in passports)


def main():
    passports = readpassports("input")
    num_valid = countvalidpassports(passports)
    print(num_valid)


if __name__ == "__main__":
    main()
