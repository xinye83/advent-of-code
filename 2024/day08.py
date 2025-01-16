import math
from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

row = len(data)
col = len(data[0])

antenna = dict()

for i in range(row):
    for j in range(col):
        if data[i][j] == ".":
            continue
        if data[i][j] in antenna:
            antenna[data[i][j]].append(i + j * row)
        else:
            antenna[data[i][j]] = [i + j * row]

# --- part 1 ---

antinode = set()

for _, value in antenna.items():
    l = len(value)

    for i in range(l - 1):
        x1 = value[i] % row
        y1 = math.floor(value[i] / row)

        for j in range(i + 1, l):
            x2 = value[j] % row
            y2 = math.floor(value[j] / row)

            x0 = 2 * x1 - x2
            y0 = 2 * y1 - y2

            if x0 >= 0 and x0 < row and y0 >= 0 and y0 < col:
                antinode.add(x0 + y0 * row)

            x0 = 2 * x2 - x1
            y0 = 2 * y2 - y1

            if x0 >= 0 and x0 < row and y0 >= 0 and y0 < col:
                antinode.add(x0 + y0 * row)

print(len(antinode))

# --- part 2 ---


def gcd(a: int, b: int) -> int:
    assert a > 0
    assert b > 0

    if a == b:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(a - b, b)


for _, value in antenna.items():
    l = len(value)

    for i in range(l - 1):
        x1 = value[i] % row
        y1 = math.floor(value[i] / row)

        for j in range(i + 1, l):
            x2 = value[j] % row
            y2 = math.floor(value[j] / row)

            # new antinodes in line with two antennas
            if x1 == x2:
                for jj in range(col):
                    antinode.add(x1 + jj * row)
                continue

            if y1 == y2:
                for ii in range(row):
                    antinode.add(ii + y1 * row)
                continue

            m = gcd(abs(x2 - x1), abs(y2 - y1))
            x0 = (x2 - x1) / m
            y0 = (y2 - y1) / m

            ii = 0
            while True:
                if (
                    x1 + ii * x0 < 0
                    or x1 + ii * x0 >= row
                    or y1 + ii * y0 < 0
                    or y1 + ii * y0 >= col
                ):
                    break
                antinode.add((x1 + ii * x0) + (y1 + ii * y0) * row)
                ii += 1

            ii = 0
            while True:
                if (
                    x1 - ii * x0 < 0
                    or x1 - ii * x0 >= row
                    or y1 - ii * y0 < 0
                    or y1 - ii * y0 >= col
                ):
                    break
                antinode.add((x1 - ii * x0) + (y1 - ii * y0) * row)
                ii += 1

print(len(antinode))
