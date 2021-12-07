from aoc21 import *
import statistics

data = read_table("input/day07.in", "string")

crab = list(map(int, data[0][0].split(",")))

pos = int(statistics.median(crab))
fuel = 0
for c in crab:
    fuel += abs(c - pos)

print(f"Part 1 - {fuel}")

# brute force
pos = 0
n = len(crab)
minval = sum(crab)

for i in range(max(crab) + 1):
    val = n * i * i - 2 * sum(crab) * i + sum([abs(i - c) for c in crab])
    if val < minval:
        minval = val
        pos = i

fuel = sum([int(abs(pos - c) * (abs(pos - c) + 1) / 2) for c in crab])

print(f"Part 2 - {fuel}")
