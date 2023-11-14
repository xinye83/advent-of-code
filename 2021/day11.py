data = open("input/day11.in", "r").read().strip("\n").split("\n")

grid = [list(map(int, list(line))) for line in data]
size = 10
steps = 100

flashes = 0

for step in range(steps):

    flashed = []

    for i in range(size):
        for j in range(size):
            grid[i][j] += 1

            if grid[i][j] > 9:
                flashed.append([i, j])

    index = 0

    while index < len(flashed):
        i = flashed[index][0]
        j = flashed[index][1]

        for i0 in [-1, 0, 1]:
            for j0 in [-1, 0, 1]:
                if i + i0 < 0 or i + i0 >= size or j + j0 < 0 or j + j0 >= size:
                    continue
                if [i + i0, j + j0] in flashed:
                    continue

                grid[i + i0][j + j0] += 1
                if grid[i + i0][j + j0] > 9:
                    flashed.append([i + i0, j + j0])

        index += 1

    for i, j in flashed:
        grid[i][j] = 0

    flashes += len(flashed)

print(f"Part 1 - {flashes}")

grid = [list(map(int, list(line))) for line in data]
step = 0

while True:
    step += 1

    flashed = []

    for i in range(size):
        for j in range(size):
            grid[i][j] += 1

            if grid[i][j] > 9:
                flashed.append([i, j])

    index = 0

    while index < len(flashed):
        i = flashed[index][0]
        j = flashed[index][1]

        for i0 in [-1, 0, 1]:
            for j0 in [-1, 0, 1]:
                if i + i0 < 0 or i + i0 >= size or j + j0 < 0 or j + j0 >= size:
                    continue
                if [i + i0, j + j0] in flashed:
                    continue

                grid[i + i0][j + j0] += 1
                if grid[i + i0][j + j0] > 9:
                    flashed.append([i + i0, j + j0])

        index += 1

    if len(flashed) == size * size:
        break

    for i, j in flashed:
        grid[i][j] = 0

print(f"Part 2 - {step}")
