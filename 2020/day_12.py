# --- Day 12: Rain Risk ---

data = []

with open("input/day_12.in", "r") as file:
    data = [line.strip("\n") for line in file]

# --- part 1 ---

# east, south, west, north
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# current direction, coordinate
d = 0
x = 0
y = 0

for line in data:
    instr = line[0]
    num = int(line[1:])

    if instr == "N":
        y += num
    elif instr == "S":
        y -= num
    elif instr == "E":
        x += num
    elif instr == "W":
        x -= num
    elif instr == "F":
        x += num * directions[d][0]
        y += num * directions[d][1]
    elif instr == "R":
        d += int(num / 90)
        d %= 4
    elif instr == "L":
        d -= int(num / 90)
        d %= 4

print(abs(x) + abs(y))


# --- part 2 ---


def rotate_way_point(instr, num, x_way, y_way):
    num %= 360

    if num == 0:
        return x_way, y_way
    elif num == 180:
        return -x_way, -y_way
    elif num == 90 and instr == "R" or num == 270 and instr == "L":
        return y_way, -x_way
    else:
        return -y_way, x_way


x_way = 10
y_way = 1

x_ship = 0
y_ship = 0

for line in data:
    instr = line[0]
    num = int(line[1:])

    if instr == "N":
        y_way += num
    elif instr == "S":
        y_way -= num
    elif instr == "E":
        x_way += num
    elif instr == "W":
        x_way -= num
    elif instr == "F":
        x_ship += num * x_way
        y_ship += num * y_way
    else:  # rotate way point
        x_way, y_way = rotate_way_point(instr, num, x_way, y_way)

print(abs(x_ship) + abs(y_ship))
