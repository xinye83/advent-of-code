data = open("input/day08.in", "r").read().strip("\n").split("\n")

count = 0

for line in data:
    for code in line.split("|")[1].split():
        if len(code) in [2, 3, 4, 7]:
            count += 1

print(f"Part 1 - {count}")

digits = {
    "cf": "1",
    "acf": "7",
    "bcdf": "4",
    "acdeg": "2",
    "acdfg": "3",  # "acf" + "dg"
    "abdfg": "5",
    "abdefg": "6",  # 8 - c
    "abcefg": "0",  # 8 - d
    "abcdfg": "9",  # 8 - e
    "abcdefg": "8",
}

total = 0

for line in data:
    code1 = sorted(line.split("|")[0].split(), key=len)
    code2 = line.split("|")[1].split()

    mapping = {}

    # find "a"
    for c in code1[1]:
        if c not in code1[0]:
            mapping[c] = "a"
            break

    # find "c", then "f"
    for c in code1[9]:
        if (
                (c not in code1[6] and c in code1[0])
                or (c not in code1[7] and c in code1[0])
                or (c not in code1[8] and c in code1[0])
        ):
            mapping[c] = "c"

            for c2 in code1[0]:
                if c2 != c:
                    mapping[c2] = "f"
                    break

            break

    # find "g" & "d"
    for i in [3, 4, 5]:
        miss = ""

        for c in code1[i]:
            if c not in mapping:
                miss += c

        if len(miss) != 2:
            continue

        for c in miss:
            if c not in code1[2]:
                mapping[c] = "g"
            else:
                mapping[c] = "d"

    # find "b"
    for c in code1[2]:
        if c not in mapping:
            mapping[c] = "b"

    # find "e"
    for c in code1[-1]:
        if c not in mapping:
            mapping[c] = "e"

    for i, code in enumerate(code2):

        temp = ""
        for c in code:
            temp += mapping[c]

        code2[i] = "".join(sorted(temp))

    code = ""

    for d in code2:
        code += digits[d]

    total += int(code)

print(f"Part 2 - {total}")
