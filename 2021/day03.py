from aoc21 import *

data = read_table("input/day03.in", "string")
codes = data[0]

count = [0 for i in range(len(codes[0]))]

for code in codes:
    for i, c in enumerate(code):
        if c == "1":
            count[i] += 1

gamma = ""
epsilon = ""

for c in count:
    if 2 * c > len(codes):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(f"Part 1 - {int(gamma, 2) * int(epsilon, 2)}")

# oxygen generator rating
oxy = codes.copy()
pos = 0

while len(oxy) > 1:
    count = 0

    for code in oxy:
        if code[pos] == "1":
            count += 1

    if count * 2 >= len(oxy):
        common = "1"
    else:
        common = "0"

    temp = oxy.copy()

    for code in oxy:
        if code[pos] != common:
            temp.remove(code)

    oxy = temp

    pos += 1
    if pos >= len(oxy[0]):
        pos = 0

# CO2 scrubber rating
co2 = codes.copy()
pos = 0

while len(co2) > 1:
    count = 0

    for code in co2:
        if code[pos] == "0":
            count += 1

    if count * 2 <= len(co2):
        least = "0"
    else:
        least = "1"

    temp = co2.copy()

    for code in co2:
        if code[pos] != least:
            temp.remove(code)

    co2 = temp

    pos += 1
    if pos >= len(co2[0]):
        pos = 0

print(f"Part 2 - {int(oxy[0], 2) * int(co2[0], 2)}")
