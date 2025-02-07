from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

map = data
row = len(map)
col = len(map[0])

start = None
end = None

for i in range(row):
    for j in range(col):
        if map[i][j] == "S":
            start = (i, j)
        elif map[i][j] == "E":
            end = (i, j)

# Dijkstra's Algorithm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode

# --- part 1 ---

# each node is denoted by (x, y, dx, dy)

dist = dict()
prev = dict()
stack = list()

for i in range(row):
    for j in range(col):
        if map[i][j] == "#":
            continue
        elif map[i][j] == "S":
            stack.append((i, j, 0, 1))
            dist[(i, j, 0, 1)] = 0
        else:
            for x0, y0 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if map[i - x0][j - y0] != "#":
                    stack.append((i, j, x0, y0))

while stack:
    node = None
    score = -1

    for item in stack:
        if item not in dist:
            continue
        if score == -1 or dist[item] < score:
            node = item
            score = dist[item]

    assert node
    stack.remove(node)

    x = node[0]
    y = node[1]
    dx = node[2]
    dy = node[3]

    if (x, y) == end:
        break

    for x0, y0 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if map[x + x0][y + y0] == "#" or (x + x0, y + y0, x0, y0) not in stack:
            continue

        if (dx, dy) == (x0, y0):
            alt = score + 1
        else:
            alt = score + 1001

        if (x + x0, y + y0, x0, y0) not in dist or dist[
            (x + x0, y + y0, x0, y0)
        ] >= alt:
            dist[(x + x0, y + y0, x0, y0)] = alt
            if (x + x0, y + y0, x0, y0) not in prev:
                prev[(x + x0, y + y0, x0, y0)] = [node]
            else:
                prev[(x + x0, y + y0, x0, y0)].append(node)

low = None

for x0, y0 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    if (end[0], end[1], x0, y0) in dist:
        if low is None or dist[(end[0], end[1], x0, y0)] < low:
            low = dist[(end[0], end[1], x0, y0)]

print(low)

# --- part 2 ---

# reconstruct shortest path(s)

stack = list()
tile = set()

for x0, y0 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    if (end[0], end[1], x0, y0) in dist and dist[(end[0], end[1], x0, y0)] == low:
        stack.append((end[0], end[1], x0, y0))

while stack:
    node = stack.pop()

    tile.add(node[0] + node[1] * row)

    if node in prev:
        stack += prev[node]

print(len(tile))
