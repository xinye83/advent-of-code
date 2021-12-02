# --- Day 3: Toboggan Trajectory ---

data = []

with open("input/day_03.in", "r") as file:
    for line in file:
        data.append(line.strip("\n"))

# --- part 1 ---

# direction
right = 3
down = 1

# dimention of the grid
row = len(data)
col = len(data[0])

# current position
x = 0
y = 0

count = 0

while True:
    x += down
    y += right

    if x >= row:
        break

    if y >= col:
        y -= col

    if data[x][y] == "#":
        count += 1

print(count)

# --- part 2 ---

directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

mul = 1

for right, down in directions:

    x = 0
    y = 0

    count = 0

    while True:
        x += down
        y += right

        if x >= row:
            break

        if y >= col:
            y -= col

        if data[x][y] == "#":
            count += 1

    mul *= count

print(mul)
