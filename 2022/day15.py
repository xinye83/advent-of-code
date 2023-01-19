import sys
from pathlib import Path


def dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


data = (Path(__file__).parent / 'input' / 'day15.in').read_text().strip('\n').split('\n')

sensor = []
beacon = []

for line in data:
    temp = line[len('Sensor at '):line.index(':')]
    temp = temp.split(', ', 1)
    sensor.append([int(temp[0][2:]), int(temp[1][2:])])

    temp = line[line.index('is at ') + len('is at '):]
    temp = temp.split(', ', 1)
    beacon.append([int(temp[0][2:]), int(temp[1][2:])])

# row is 10 when using day15_ex.in
row = 2000000

pos = set()
bea = set()

for i in range(len(sensor)):
    if beacon[i][1] == row:
        bea.add(beacon[i][0])

    if dist(sensor[i], beacon[i]) < abs(sensor[i][1] - row):
        continue

    for j in range(dist(sensor[i], beacon[i]) - abs(sensor[i][1] - row) + 1):
        pos.add(sensor[i][0] + j)
        pos.add(sensor[i][0] - j)

print(len(pos) - len(bea))

# part 2

search = 4000000


def check_position(x, y):
    if x < 0 or x > search or y < 0 or y > search:
        return

    for i in range(len(sensor)):
        if dist([x, y], sensor[i]) <= dist(sensor[i], beacon[i]):
            return

    print(x * search + y)
    sys.exit()


for i in range(len(sensor)):
    d = dist(sensor[i], beacon[i])

    for j in range(d + 1):
        x = sensor[i][0] + d + 1 - j
        y = sensor[i][1] + j
        check_position(x, y)

        x = sensor[i][0] - j
        y = sensor[i][1] + d + 1 - j
        check_position(x, y)

        x = sensor[i][0] - d - 1 + j
        y = sensor[i][1] - j
        check_position(x, y)

        x = sensor[i][0] + j
        y = sensor[i][1] - d - 1 + j
        check_position(x, y)
