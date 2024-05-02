import re
from util import *

data = get_input().split("\n")

# --- part 1 ---
value = 0

row = len(data)
col = len(data[0])

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
