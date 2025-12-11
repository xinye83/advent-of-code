from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

# --- part 1 ---

red_tiles = [tuple(map(int, line.split(","))) for line in data]

area = 0

for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        area = max(
            area,
            (abs(red_tiles[i][0] - red_tiles[j][0]) + 1)
            * (abs(red_tiles[i][1] - red_tiles[j][1]) + 1),
        )

print(area)

# --- part 2 ---

# map to reduced coordinate system

X = [tile[0] for tile in red_tiles]
X = list(set(X))
X.sort()

Y = [tile[1] for tile in red_tiles]
Y = list(set(Y))
Y.sort()


def new_coordinate_helper(x: int, X: list[int]) -> int:
    i = 0
    while i < len(X):
        if x < X[i]:
            return 2 * i
        elif x == X[i]:
            return 2 * i + 1
        else:
            i += 1

    return 2 * len(X)


def new_coordinate(x: int, y: int) -> tuple[int, int]:
    return new_coordinate_helper(x, X), new_coordinate_helper(y, Y)


red_tiles_new = [new_coordinate(tile[0], tile[1]) for tile in red_tiles]

# now do everything in new coordinate system

# collect edge tiles

red_tiles_new.append(red_tiles_new[0])

xmin = red_tiles_new[0][0]
xmax = red_tiles_new[0][0]
ymin = red_tiles_new[0][1]
ymax = red_tiles_new[0][1]

edges = dict()

for i in range(len(red_tiles_new) - 1):
    x1, y1 = red_tiles_new[i]
    x2, y2 = red_tiles_new[i + 1]

    xmin = min(xmin, x1)
    xmax = max(xmax, x1)
    ymin = min(ymin, y1)
    ymax = max(ymax, y1)

    if x1 == x2:
        if x1 not in edges:
            edges[x1] = [y for y in range(min(y1, y2), max(y1, y2) + 1)]
        else:
            edges[x1] += [y for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if x not in edges:
                edges[x] = [y1]
            else:
                edges[x].append(y1)
    else:
        raise Exception()

IN = set()
OUT = set()


def map2int(x: int, y: int) -> int:
    return (x - xmin) * (ymax - ymin + 1) + (y - ymin)


for k, v in edges.items():
    for i in v:
        IN.add(map2int(k, i))


def in_polygon(x: int, y: int) -> bool:
    num = map2int(x, y)

    if num in IN:
        return True
    elif num in OUT:
        return False

    for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        l = 1
        while True:
            xnew = x + direction[0] * l
            ynew = y + direction[1] * l

            if map2int(xnew, ynew) in OUT or not (
                xmin <= xnew <= xmax and ymin <= ynew <= ymax
            ):
                for i in range(l + 1):
                    OUT.add(map2int(x + direction[0] * i, y + direction[1] * i))
                return False

            if map2int(xnew, ynew) in IN:
                break

            l += 1

    IN.add(num)
    return True


area2 = 0

for i in range(len(red_tiles_new) - 1):
    for j in range(i + 1, len(red_tiles_new) - 1):

        x1, y1 = red_tiles_new[i]
        x2, y2 = red_tiles_new[j]

        interior = True

        for x in range(min(x1, x2), max(x1, x2) + 1):
            if not in_polygon(x, y1):
                interior = False
                break
            if not in_polygon(x, y2):
                interior = False
                break

        if not interior:
            continue

        for y in range(min(y1, y2), max(y1, y2) + 1):
            if not in_polygon(x1, y):
                interior = False
                break
            if not in_polygon(x2, y):
                interior = False
                break

        if not interior:
            continue

        # calculate the area with the original coordinate system
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]

        area2 = max(
            area2,
            (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1),
        )

print(area2)
