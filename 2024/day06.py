import copy
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

# row_map[i] contains column indices of obstacles in row i
row_map = {}
# col_map[j] contains row indices of obstacles in column j
col_map = {}

x_org = -1
y_org = -1

for i in range(row):
    for j in range(col):
        if data[i][j] == "^":
            x_org = i
            y_org = j
        elif data[i][j] == "#":
            if i in row_map:
                row_map[i].append(j)
            else:
                row_map[i] = [j]
            if j in col_map:
                col_map[j].append(i)
            else:
                col_map[j] = [i]

for key, val in col_map.items():
    col_map[key].sort()

# --- part 1 ---

# map location (x, y) to x + y * row
path = set()  # path of the guard
path.add(x_org + y_org * row)

# guard is at (x, y) with direction d
# d = 0 ==> up
# d = 1 ==> right
# d = 2 ==> down
# d = 3 ==> left
d = 0

x = x_org
y = y_org

while True:
    # next direction
    d1 = d + 1
    if d1 == 4:
        d1 = 0

    if d == 0:
        try:
            x1 = max([i for i in col_map[y] if i < x])
        except:
            x1 = -1

        for x0 in range(x1 + 1, x):
            path.add(x0 + y * row)

        x = x1 + 1
        y1 = y
    elif d == 1:
        try:
            y1 = min([j for j in row_map[x] if j > y])
        except:
            y1 = col

        for y0 in range(y + 1, y1):
            path.add(x + y0 * row)

        y = y1 - 1
        x1 = x
    elif d == 2:
        try:
            x1 = min([i for i in col_map[y] if i > x])
        except:
            x1 = row

        for x0 in range(x + 1, x1):
            path.add(x0 + y * row)

        x = x1 - 1
        y1 = y
    elif d == 3:
        try:
            y1 = max([j for j in row_map[x] if j < y])
        except:
            y1 = -1

        for y0 in range(y1 + 1, y):
            path.add(x + y0 * row)

        y = y1 + 1
        x1 = x

    if x == 0 or x == row - 1 or y == 0 or y == col - 1:
        break

    d = d1

print(len(path))

# --- part 2 ---


# input:
#   loc: new obstacle location
# output:
#   if the new obstacle can create loop
def is_loop(loc: int) -> bool:
    x = x_org
    y = y_org
    d = 0

    x0 = loc % row
    y0 = math.floor(loc / row)

    row_map_1 = copy.deepcopy(row_map)
    col_map_1 = copy.deepcopy(col_map)

    if x0 not in row_map_1:
        row_map_1[x0] = [y0]
    else:
        row_map_1[x0].append(y0)
        row_map_1[x0].sort()

    if y0 not in col_map_1:
        col_map_1[y0] = [x0]
    else:
        col_map_1[y0].append(x0)
        col_map_1[y0].sort()

    # map obstacle (x, y, d) to (x + y * row) * 4 + d
    obs = set()  # obstacle in guard's path

    while True:
        # next direction
        d1 = d + 1
        if d1 == 4:
            d1 = 0

        if d == 0:
            try:
                x1 = max([i for i in col_map_1[y] if i < x])
            except:
                return False
            x = x1 + 1
            y1 = y
        elif d == 1:
            try:
                y1 = min([j for j in row_map_1[x] if j > y])
            except:
                return False
            y = y1 - 1
            x1 = x
        elif d == 2:
            try:
                x1 = min([i for i in col_map_1[y] if i > x])
            except:
                return False
            x = x1 - 1
            y1 = y
        elif d == 3:
            try:
                y1 = max([j for j in row_map_1[x] if j < y])
            except:
                return False
            y = y1 + 1
            x1 = x

        if (x1 + y1 * row) * 4 + d in obs:
            return True
        else:
            obs.add((x1 + y1 * row) * 4 + d)

        d = d1


new = 0

for loc in path:
    if is_loop(loc):
        new += 1

print(new)
