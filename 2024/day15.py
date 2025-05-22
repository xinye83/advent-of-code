from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n\n")
)

# --- part 1 ---

map = [list(row) for row in data[0].split("\n")]
move = "".join(data[1])

row = len(map)
col = len(map[0])

x = 0
y = 0

for x in range(row):
    for y in range(col):
        if map[x][y] == "@":
            break
    if map[x][y] == "@":
        break


def push(x0, y0):
    global x, y
    assert map[x][y] == "@"

    move = True
    len = 0

    while True:
        match map[x + (len + 1) * x0][y + (len + 1) * y0]:
            case ".":
                break
            case "O":
                len += 1
            case "#":
                move = False
                break

    if not move:
        return

    map[x][y] = "."
    map[x + x0][y + y0] = "@"

    if len:
        map[x + (len + 1) * x0][y + (len + 1) * y0] = "O"

    x += x0
    y += y0


for c in move:
    match c:
        case "^":
            push(-1, 0)
        case "v":
            push(1, 0)
        case "<":
            push(0, -1)
        case ">":
            push(0, 1)
        case _:
            continue

gps = 0

for i in range(row):
    for j in range(col):
        if map[i][j] == "O":
            gps += 100 * i + j

print(gps)

# --- part 2 ---


def convert(c):
    match c:
        case "#":
            return "##"
        case "O":
            return "[]"
        case ".":
            return ".."
        case "@":
            return "@."
        case _:
            raise Exception


map2 = []
for row in data[0].split("\n"):
    new = ""
    for c in row:
        new += convert(c)
    map2.append(list(new))


move2 = "".join(data[1])

row2 = len(map2)
col2 = len(map2[0])

x = 0
y = 0

for x in range(row2):
    for y in range(col2):
        if map2[x][y] == "@":
            break
    if map2[x][y] == "@":
        break


def push2_updown(direction):
    global x, y
    assert map2[x][y] == "@"

    move = True
    boxes = [set()]
    boxes[0].add(x + y * row2)

    x0 = x + direction
    while True:
        new_boxes = set()
        for box in boxes[-1]:
            y0 = int((box - x0 + direction) / row2)
            if map2[x0][y0] == "#":
                move = False
                break
            elif map2[x0][y0] == "[":
                new_boxes.add(x0 + y0 * row2)
                new_boxes.add(x0 + (y0 + 1) * row2)
            elif map2[x0][y0] == "]":
                new_boxes.add(x0 + y0 * row2)
                new_boxes.add(x0 + (y0 - 1) * row2)

        if not move or not new_boxes:
            break

        boxes.append(new_boxes)
        x0 += direction

    if not move:
        return

    # move everything in boxes upwards
    for row in boxes[::-1]:
        for i in row:
            x0 = i % row2
            y0 = int((i - x0) / row2)

            map2[x0 + direction][y0] = map2[x0][y0]
            map2[x0][y0] = "."

    x += direction


def push2_leftright(direction):
    global x, y
    assert map2[x][y] == "@"

    move = True
    len = 1

    while True:
        match map2[x][y + len * direction]:
            case "#":
                move = False
                break
            case ".":
                break
            case "[":
                len += 2
            case "]":
                len += 2

    if not move:
        return

    for y0 in range(len)[::-1]:
        map2[x][y + (y0 + 1) * direction] = map2[x][y + y0 * direction]
        map2[x][y + y0 * direction] = "."

    y += direction


for c in move2:
    match c:
        case "^":
            push2_updown(-1)
        case "v":
            push2_updown(1)
        case "<":
            push2_leftright(-1)
        case ">":
            push2_leftright(1)
        case _:
            continue

gps2 = 0

for i in range(row2):
    for j in range(col2):
        if map2[i][j] == "[":
            gps2 += 100 * i + j

print(gps2)
