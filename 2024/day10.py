from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

row = len(data)
col = len(data[0])

# --- part 1 ---

trails = list()

for i in range(row):
    for j in range(col):
        if data[i][j] == "0":
            trails.append([[i, j]])

while trails and len(trails[0]) < 10:
    path = trails.pop(0)

    h = len(path)
    i = path[-1][0]
    j = path[-1][1]

    if i > 0 and data[i - 1][j] == str(h):
        trails.append(path + [[i - 1, j]])
    if i < row - 1 and data[i + 1][j] == str(h):
        trails.append(path + [[i + 1, j]])
    if j > 0 and data[i][j - 1] == str(h):
        trails.append(path + [[i, j - 1]])
    if j < col - 1 and data[i][j + 1] == str(h):
        trails.append(path + [[i, j + 1]])

# (x, y) -> x + y * row
heads = dict()
for path in trails:
    head = path[0][0] + path[0][1] * row
    tail = path[-1][0] + path[-1][1] * row

    if head not in heads:
        heads[head] = set()

    heads[head].add(tail)

score = 0
for head in heads:
    score += len(heads[head])

print(score)

# --- part 2 ---

print(len(trails))
