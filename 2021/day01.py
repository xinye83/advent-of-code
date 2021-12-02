from aoc21 import *

data = read_file("input/day01.in", "integer")
depth = data[0]

count = 0

for i, d in enumerate(depth):
    if i > 0 and d > depth[i-1]:
        count += 1

print(f"Part 1 - {count}")

count = 0

for i, d in enumerate(depth):
    if i > 2 and d > depth[i-3]:
        count += 1

print(f"Part 2 - {count}")
