from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

size = 71

# --- part 1 ---

bytes = [[int(i) for i in byte.split(",")] for byte in data[:1024]]

stack = []
dist = [[size * size for _ in range(size)] for _ in range(size)]
dist[0][0] = 0

for i in range(size):
    for j in range(size):
        if [i, j] not in bytes:
            stack.append([i, j])

while stack:
    x = -1
    y = -1
    m = size * size

    for i, j in stack:
        if dist[i][j] < m:
            x = i
            y = j
            m = dist[i][j]

    if x == size - 1 and y == size - 1:
        break

    stack.remove([x, y])

    for x0, y0 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if [x + x0, y + y0] not in stack:
            continue
        dist[x + x0][y + y0] = min(dist[x + x0][y + y0], dist[x][y] + 1)

print(dist[size - 1][size - 1])

# --- part 2 ---

num = 1023
reach = True
path = [None] * (size * size)
i = 0
j = 0

bytes = [x + y * size for x, y in bytes]

while reach:
    num += 1
    new_byte = int(data[num].split(",")[0]) + int(data[num].split(",")[1]) * size
    bytes.append(new_byte)

    if j > 0 and new_byte not in path[:j]:
        continue
    elif j == 0:
        path[i] = 0
        i = 0
        j = 1
    else:
        i = 0
        j = path.index(new_byte)

    reach = False

    while i < j:
        x = path[i] % size
        y = int((path[i] - x) / size)
        if x == size - 1 and y == size - 1:
            reach = True
        for x0, y0 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not (0 <= x + x0 < size and 0 <= y + y0 < size):
                continue
            if (
                x + x0 + (y + y0) * size in path[:j]
                or x + x0 + (y + y0) * size in bytes
            ):
                continue
            path[j] = x + x0 + (y + y0) * size
            j += 1
        i += 1

print(data[num])
