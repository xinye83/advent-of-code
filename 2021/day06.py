from aoc21 import *

data = read_table("input/day06.in", "string")

fish = list(map(int, data[0][0].split(",")))
days = 80

for _ in range(days):
    l = len(fish)
    for i in range(l):
        if fish[i] == 0:
            fish[i] = 6
            fish += [8]
        else:
            fish[i] -= 1

print(f"Part 1 - {len(fish)}")

fish = list(map(int, data[0][0].split(",")))
days = 256

count = [0 for i in range(9)]
for i in fish:
    count[i] += 1

for i in range(days):
    count = count[1:] + [count[0]]
    count[6] += count[8]

print(f"Part 2 - {sum(count)}")
