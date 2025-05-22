from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

col = 50
row = 6

# x -> column 0, column 1, ..., column 49

#  y
#  |
#  v
# row 0
# row 1
# row 2
# .....

# screen[y][x]

# --- part 1 ---

screen = [["." for _ in range(col)] for _ in range(row)]

for line in data:
    if line[:4] == "rect":
        x, y = line[4:].strip().split("x")
        x = int(x)
        y = int(y)

        for i in range(x):
            for j in range(y):
                screen[j][i] = "#"
    elif line[:13] == "rotate column":
        x, p = line[16:].split(" by ")
        x = int(x)
        p = int(p)

        temp = [screen[j][x] for j in range(row)]

        for j in range(row):
            screen[(j + p) % row][x] = temp[j]
    elif line[:10] == "rotate row":
        y, p = line[13:].split(" by ")
        y = int(y)
        p = int(p)

        temp = [screen[y][i] for i in range(col)]

        for i in range(col):
            screen[y][(i + p) % col] = temp[i]

num = 0

for i in range(col):
    for j in range(row):
        num += screen[j][i] == "#"

print(num)

# --- part 2 ---

for j in range(row):
    for i in range(col):
        print(screen[j][i], end="")
    print()
