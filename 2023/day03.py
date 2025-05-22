import re
from util import *

data = get_input().split("\n")

row = len(data)
col = len(data[0])

# --- part 1 ---
value = 0

r = 0

for line in data:
    for match in re.finditer("\d+", line):
        temp = ""
        if r > 0 and match.start() > 0:
            temp += data[r - 1][match.start() - 1]
        if r > 0:
            temp += data[r - 1][match.start() : match.end()]
        if r > 0 and match.end() < col - 1:
            temp += data[r - 1][match.end()]
        if match.start() > 0:
            temp += data[r][match.start() - 1]
        if match.end() < col - 1:
            temp += data[r][match.end()]
        if r < row - 1 and match.start() > 0:
            temp += data[r + 1][match.start() - 1]
        if r < row - 1:
            temp += data[r + 1][match.start() : match.end()]
        if r < row - 1 and match.end() < col - 1:
            temp += data[r + 1][match.end()]

        if re.sub("\d|\.", "", temp):
            value += int(data[r][match.start() : match.end()])

    r += 1

print(value)

# --- part 2 ---
gear = {}

r = 0

for line in data:
    for match in re.finditer("\d+", line):
        number = int(line[match.start() : match.end()])

        neighbor = []
        if r > 0 and match.start() > 0:
            neighbor.append((r - 1, match.start() - 1))
        if r > 0:
            for i in range(match.start(), match.end()):
                neighbor.append((r - 1, i))
        if r > 0 and match.end() < col - 1:
            neighbor.append((r - 1, match.end()))
        if match.start() > 0:
            neighbor.append((r, match.start() - 1))
        if match.end() < col - 1:
            neighbor.append((r, match.end()))
        if r < row - 1 and match.start() > 0:
            neighbor.append((r + 1, match.start() - 1))
        if r < row - 1:
            for i in range(match.start(), match.end()):
                neighbor.append((r + 1, i))
        if r < row - 1 and match.end() < col - 1:
            neighbor.append((r + 1, match.end()))

        for temp in neighbor:
            if data[temp[0]][temp[1]] == "*":
                if temp not in gear:
                    gear[temp] = [number]
                else:
                    gear[temp].append(number)

    r += 1

value = 0

for key in gear:
    if len(gear[key]) == 2:
        value += gear[key][0] * gear[key][1]

print(value)
