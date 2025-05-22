from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

map = data
row = len(data)
col = len(data[0])

# --- part 1 ---

# construct the racetrack

for i in range(row):
    for j in range(col):
        if map[i][j] == "S":
            start = (i, j)
        elif map[i][j] == "E":
            end = (i, j)

track = [start]

while track[-1] != end:
    x = track[-1][0]
    y = track[-1][1]

    for x0, y0 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if not (0 <= x + x0 < row and 0 <= y + y0 < col):
            continue
        if map[x + x0][y + y0] == "#" or (x + x0, y + y0) in track:
            continue
        track.append((x + x0, y + y0))
        break

length = len(track) - 1

# search for cheats

cheat2 = 0
second = 100

for i in range(len(track)):
    if length - i < second:
        continue

    x = track[i][0]
    y = track[i][1]

    for x0, y0 in (
        (2, 0),
        (1, 1),
        (0, 2),
        (-1, 1),
        (-2, 0),
        (-1, -1),
        (0, -2),
        (1, -1),
    ):
        if not (0 <= x + x0 < row and 0 <= y + y0 < col):
            continue
        if (x + x0, y + y0) in track and track.index(
            (x + x0, y + y0)
        ) - i >= 2 + second:
            cheat2 += 1


print(cheat2)

# --- part 2 ---

cheat20 = 0

for i in range(len(track) - 1):
    for j in range(i + 1, len(track)):
        d = abs(track[i][0] - track[j][0]) + abs(track[i][1] - track[j][1])
        if j - i <= second:
            continue
        if d > 20:
            continue
        if j - i >= second + d:
            cheat20 += 1

print(cheat20)
