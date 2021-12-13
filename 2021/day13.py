from aoc21 import *

data = open("input/day13.in", "r").read().strip("\n").split("\n\n")
dots = [list(map(int, dot.split(","))) for dot in data[0].split("\n")]

xmax = 0
ymax = 0
for dot in dots:
    xmax = max(xmax, dot[0])
    ymax = max(ymax, dot[1])

instructions = data[1].split("\n")

paper = []
line = instructions[0].strip("\n").split("=")
line = int(line[1])

if instructions[0][11] == "x":
    for dot in dots:
        if dot[0] > line:
            dot[0] = xmax - dot[0]
        if dot not in paper:
            paper.append(dot)
else:
    for dot in dots:
        if dot[1] > line:
            dot[1] = ymax - dot[1]
        if dot not in paper:
            paper.append(dot)

print(f"Part 1 - {len(paper)}")

curr = dots.copy()

for instruction in instructions:
    line = instruction.strip("\n").split("=")
    line = int(line[1])

    next = []

    xmax = 0
    ymax = 0
    for dot in curr:
        xmax = max(xmax, dot[0])
        ymax = max(ymax, dot[1])

    if instruction[11] == "x":
        for dot in curr:
            if dot[0] > line:
                dot[0] = xmax - dot[0]
            if dot not in next:
                next.append(dot)
    else:
        for dot in curr:
            if dot[1] > line:
                dot[1] = ymax - dot[1]
            if dot not in next:
                next.append(dot)

    curr = next.copy()

xmin = 1e9
ymin = 1e9
xmax = 0
ymax = 0

for dot in curr:
    xmin = min(xmin, dot[0])
    ymin = min(ymin, dot[1])
    xmax = max(xmax, dot[0])
    ymax = max(ymax, dot[1])

curr = [[dot[0] - xmin, dot[1] - ymin] for dot in curr]
xmax -= xmin
ymax -= ymin

print("Part 2")
for j in range(ymax + 1):
    for i in range(xmax + 1):
        if [i, j] in curr:
            print("#", end="")
        else:
            print(".", end="")

    print("\n", end="")
