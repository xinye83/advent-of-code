from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day14.in').read_text().strip('\n').split('\n')

stones = set()
for line in data:
    path = line.split(' -> ')

    i = 0
    while i < len(path) - 1:
        start = [int(k) for k in path[i].split(',')]
        end = [int(k) for k in path[i + 1].split(',')]

        if start[0] == end[0]:
            for k in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                stones.add((start[0], k))
        else:
            for k in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                stones.add((k, start[1]))

        i += 1

left = 500
right = 500
bottom = 0

for stone in stones:
    left = min(left, stone[0])
    right = max(right, stone[0])
    bottom = max(bottom, stone[1])

start = (500, 0)
void = False
sands = set()

while not void:
    rest = False
    sand = list(start)

    while not rest:
        if sand[1] >= bottom:
            void = True
            break

        if (sand[0], sand[1] + 1) not in sands and (sand[0], sand[1] + 1) not in stones:
            sand[1] += 1
            continue
        if (sand[0] - 1, sand[1] + 1) not in sands and (sand[0] - 1, sand[1] + 1) not in stones:
            sand[0] -= 1
            sand[1] += 1
            continue
        if (sand[0] + 1, sand[1] + 1) not in sands and (sand[0] + 1, sand[1] + 1) not in stones:
            sand[0] += 1
            sand[1] += 1
            continue

        sands.add((sand[0], sand[1]))
        rest = True

print(len(sands))

# part 2

left = 500
right = 500
bottom = 0

for stone in stones:
    left = min(left, stone[0])
    right = max(right, stone[0])
    bottom = max(bottom, stone[1])

bottom += 2

start = (500, 0)
sands = set()

while start not in sands:
    rest = False
    sand = list(start)

    while not rest:
        if sand[1] == bottom - 1:
            sands.add((sand[0], sand[1]))
            break

        if (sand[0], sand[1] + 1) not in sands and (sand[0], sand[1] + 1) not in stones:
            sand[1] += 1
            continue
        if (sand[0] - 1, sand[1] + 1) not in sands and (sand[0] - 1, sand[1] + 1) not in stones:
            sand[0] -= 1
            sand[1] += 1
            continue
        if (sand[0] + 1, sand[1] + 1) not in sands and (sand[0] + 1, sand[1] + 1) not in stones:
            sand[0] += 1
            sand[1] += 1
            continue

        sands.add((sand[0], sand[1]))
        rest = True

print(len(sands))
