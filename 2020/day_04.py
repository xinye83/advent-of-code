# --- Day 4: Passport Processing ---

data = []

with open("input/day_04.in", "r") as file:
    temp = file.read().split("\n\n")

    for passport in temp:

        temp2 = passport.replace("\n", " ").split()

        temp3 = {}

        for item in temp2:
            i = item.find(":")

            temp3[item[:i]] = item[i + 1:]

        data.append(temp3)

# --- part 1 ---

count = 0

for passport in data:

    valid = True

    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:

        if key not in passport:
            valid = False
            break

    if valid:
        count += 1

print(count)

# --- part 2 ---

count = 0

for passport in data:

    # check 'byr'

    if (
            not "byr" in passport
            or not len(passport["byr"]) == 4
            or not ((int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002))
    ):
        continue

    # check 'iyr'

    if (
            not "iyr" in passport
            or not len(passport["iyr"]) == 4
            or not ((int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020))
    ):
        continue

    # check 'eyr'

    if (
            not "eyr" in passport
            or not len(passport["eyr"]) == 4
            or not ((int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030))
    ):
        continue

    # check 'hgt'

    if not "hgt" in passport:
        continue

    if not passport["hgt"][-2:] in ["cm", "in"]:
        continue

    if passport["hgt"][-2:] == "cm" and not (
            int(passport["hgt"][:-2]) >= 150 and int(passport["hgt"][:-2]) <= 193
    ):
        continue

    if passport["hgt"][-2:] == "in" and not (
            int(passport["hgt"][:-2]) >= 59 and int(passport["hgt"][:-2]) <= 76
    ):
        continue

    # check 'hcl'

    if (
            not "hcl" in passport
            or not len(passport["hcl"]) == 7
            or not passport["hcl"][0] == "#"
    ):
        continue

    try:
        int(passport["hcl"][1:], 16)
    except:
        continue

    # check 'ecl'

    if not "ecl" in passport or not passport["ecl"] in [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]:
        continue

    # check 'pid'

    if not "pid" in passport or not len(passport["pid"]) == 9:
        continue

    try:
        int(passport["pid"])
    except:
        continue

    # passed all checks

    count += 1

print(count)
