from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split(",")
)

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

# --- part 1 ---

x = 0
y = 0
i = 0

for step in data:
    step = step.strip()
    turn = step[0]
    length = int(step[1:])

    if turn == "R":
        i = (i + 1) % 4
    else:
        i = (i - 1) % 4

    x += length * direction[i][0]
    y += length * direction[i][1]

print(abs(x) + abs(y))

# --- part 2 ---

x = 0
y = 0
i = 0

visited = [[0, 0]]
found = False

for step in data:
    step = step.strip()
    turn = step[0]
    length = int(step[1:])

    if turn == "R":
        i = (i + 1) % 4
    else:
        i = (i - 1) % 4

    for _ in range(length):
        x += direction[i][0]
        y += direction[i][1]

        if [x, y] in visited:
            found = True
            break
        else:
            visited.append([x, y])

    if found:
        break

print(abs(x) + abs(y))
