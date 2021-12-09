from aoc21 import *

data = open("input/day09.in", "r").read().strip("\n").split("\n")
heightmap = [list(map(int, list(line))) for line in data]

row = len(heightmap)
col = len(heightmap[0])

risk = 0

for i in range(row):
    for j in range(col):
        if i > 0 and heightmap[i][j] >= heightmap[i - 1][j]:
            continue

        if i < row - 1 and heightmap[i][j] >= heightmap[i + 1][j]:
            continue

        if j > 0 and heightmap[i][j] >= heightmap[i][j - 1]:
            continue

        if j < col - 1 and heightmap[i][j] >= heightmap[i][j + 1]:
            continue

        risk += heightmap[i][j] + 1

print(f"Part 1 - {risk}")

basin = []

for i in range(row):
    for j in range(col):
        if i > 0 and heightmap[i][j] >= heightmap[i - 1][j]:
            continue

        if i < row - 1 and heightmap[i][j] >= heightmap[i + 1][j]:
            continue

        if j > 0 and heightmap[i][j] >= heightmap[i][j - 1]:
            continue

        if j < col - 1 and heightmap[i][j] >= heightmap[i][j + 1]:
            continue

        stack = [[i, j]]
        index = 0

        while index < len(stack):
            i0 = stack[index][0]
            j0 = stack[index][1]

            if i0 > 0 and [i0 - 1, j0] not in stack and heightmap[i0 - 1][j0] < 9:
                stack.append([i0 - 1, j0])

            if i0 < row - 1 and [i0 + 1, j0] not in stack and heightmap[i0 + 1][j0] < 9:
                stack.append([i0 + 1, j0])

            if j0 > 0 and [i0, j0 - 1] not in stack and heightmap[i0][j0 - 1] < 9:
                stack.append([i0, j0 - 1])

            if j0 < col - 1 and [i0, j0 + 1] not in stack and heightmap[i0][j0 + 1] < 9:
                stack.append([i0, j0 + 1])

            index += 1

        basin.append(index)

basin.sort()

print(f"Part 2 - {basin[-1] * basin[-2] * basin[-3]}")
