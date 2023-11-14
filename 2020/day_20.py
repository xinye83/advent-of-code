# --- Day 20: Jurassic Jigsaw ---

data = open("input/day_20.in", "r").read().strip("\n").split("\n\n")


class Tile:
    def __init__(self, grid, neighbor):
        self.grid = grid
        self.neighbor = neighbor
        self.edge = [[], [], [], []]


tiles = {}

for item in data:
    j = item.find("\n")

    id = int(item[5: j - 1])
    image = item[j + 1:].split("\n")

    tiles[id] = Tile(image, 0)

# --- part 1 ---

# find matching edges
edges = {}

for id in tiles:

    top = tiles[id].grid[0]
    bottom = tiles[id].grid[-1][::-1]

    left = ""
    right = ""
    for line in tiles[id].grid:
        left = line[0] + left
        right += line[-1]

    for edge, side in zip([top, right, bottom, left], [0, 1, 2, 3]):
        if edge not in edges and edge[::-1] not in edges:
            edges[edge] = [[id, side, True]]
        elif edge in edges:
            edges[edge].append([id, side, True])
        else:
            edges[edge[::-1]].append([id, side, False])  # False ==> reverse

for edge in edges:
    if len(edges[edge]) == 2:
        tiles[edges[edge][0][0]].neighbor += 1
        tiles[edges[edge][1][0]].neighbor += 1

prod = 1
for id in tiles:
    if tiles[id].neighbor == 2:
        prod *= id

print(prod)

# --- part 2 ---

for edge in edges:
    if len(edges[edge]) == 2:
        id0 = edges[edge][0][0]
        side0 = edges[edge][0][1]
        rev0 = edges[edge][0][2]

        id1 = edges[edge][1][0]
        side1 = edges[edge][1][1]
        rev1 = edges[edge][1][2]

        tiles[id0].edge[side0] = [id1, side1, rev0 == rev1]
        tiles[id1].edge[side1] = [id0, side0, rev0 == rev1]

for id in tiles:
    if tiles[id].neighbor == 2:
        break

# place this tile at the top-left corner of the image
# this tile has edge matches at bottom and left

grid = [[]]
