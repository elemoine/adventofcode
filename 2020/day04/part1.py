requiredfields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def parseline(line):
    info = {}
    pairs = line.split()
    for pair in pairs:
        k, v = pair.split(":")
        info[k] = v
    return info


def readpassports(filename):
    passports, passport = [], None
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                info = parseline(line)
                if passport:
                    passport.update(info)
                else:
                    passport = info
            elif passport:
                passports.append(passport)
                passport = None
        if passport:
            passports.append(passport)
    return passports


def countvalidpassports(passports):
    return sum(int(requiredfields <= set(passport.keys())) for passport in passports)


def main():
    passports = readpassports("input")
    num_valid = countvalidpassports(passports)
    print(num_valid)


if __name__ == "__main__":
    main()
