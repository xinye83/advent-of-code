from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---

# keypad
# 1 2 3    (0,2) (1,2) (2,2)
# 4 5 6 -> (0,1) (1,1) (2,1)
# 7 8 9    (0,0) (1,0) (2,0)

keypad = ("741", "852", "963")


def move(x: int, y: int, sequence: str) -> tuple[int, int]:
    assert 0 <= x < 3
    assert 0 <= y < 3

    if len(sequence) > 1:
        for s in sequence:
            x, y = move(x, y, s)
        return x, y

    s = sequence
    assert s in "UDLR"

    if s == "U":
        y += 1
    elif s == "D":
        y -= 1
    elif s == "L":
        x -= 1
    elif s == "R":
        x += 1

    return min(max(x, 0), 2), min(max(y, 0), 2)


x = 1
y = 1

code = ""

for sequence in data:
    x, y = move(x, y, sequence)
    code += keypad[x][y]

print(code)

# --- part 2 ---

# keypad
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

keypad2 = ("  5  ", " A62 ", "DB731", " C84 ", "  9  ")


def move2(x: int, y: int, sequence: str) -> tuple[int, int]:
    assert 0 <= x < 5
    assert 0 <= y < 5

    if len(sequence) > 1:
        for s in sequence:
            x, y = move2(x, y, s)
        return x, y

    s = sequence
    assert s in "UDLR"

    x1 = x
    y1 = y
    if s == "U":
        y1 += 1
    elif s == "D":
        y1 -= 1
    elif s == "L":
        x1 -= 1
    elif s == "R":
        x1 += 1

    if not (0 <= x1 < 5) or not (0 <= y1 < 5) or keypad2[x1][y1] == " ":
        x1 = x
        y1 = y

    return x1, y1


x = 0
y = 2

code2 = ""

for sequence in data:
    x, y = move2(x, y, sequence)
    code2 += keypad2[x][y]

print(code2)
