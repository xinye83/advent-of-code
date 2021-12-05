from aoc21 import *
from collections import defaultdict

data = read_table("input/day05.in", "string", "string", "string")
vents = [
    list(map(int, p1.split(",") + p2.split(","))) for (p1, p2) in zip(data[0], data[2])
]

overlap = defaultdict(int)

for vent in vents:
    if vent[0] == vent[2] or vent[1] == vent[3]:
        for x in range(min(vent[0], vent[2]), max(vent[0], vent[2]) + 1):
            for y in range(min(vent[1], vent[3]), max(vent[1], vent[3]) + 1):
                overlap[x, y] += 1

count = 0

for key, value in overlap.items():
    if value >= 2:
        count += 1

print(f"Part 1 - {count}")

overlap = defaultdict(int)

for vent in vents:
    if vent[0] == vent[2] or vent[1] == vent[3]:
        for x in range(min(vent[0], vent[2]), max(vent[0], vent[2]) + 1):
            for y in range(min(vent[1], vent[3]), max(vent[1], vent[3]) + 1):
                overlap[x, y] += 1
    elif abs(vent[0] - vent[2]) == abs(vent[1] - vent[3]):
        if vent[0] < vent[2]:
            x = 1
        else:
            x = -1

        if vent[1] < vent[3]:
            y = 1
        else:
            y = -1

        for z in range(abs(vent[0] - vent[2]) + 1):
            overlap[vent[0] + x * z, vent[1] + y * z] += 1


count = 0

for key, value in overlap.items():
    if value >= 2:
        count += 1

print(f"Part 2 - {count}")
