from aoc21 import *

data = read_file("input/day02.in", "string", "integer")
instruction = data[0]
step_size = data[1]

x = 0
y = 0

for i, s in zip(instruction, step_size):
    if i == "forward":
        x += s
    elif i == "up":
        y -= s
    else:
        y += s

print(f"Part 1 - {x * y}")

aim = 0
pos = 0
dep = 0

for i, s in zip(instruction, step_size):
    if i == "forward":
        pos += s
        dep += aim * s
    elif i == "up":
        aim -= s
    else:
        aim += s

print(f"Part 2 - {pos * dep}")
