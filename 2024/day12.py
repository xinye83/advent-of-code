from pathlib import Path
import copy

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

row = len(data)
col = len(data)

# --- part 1 ---


def update_perimeter(new: int, garden: list[int]) -> int:
    x = new % row
    y = int((new - x) / row)

    n = 0
    if x + 1 + y * row in garden:
        n += 1
    if x - 1 + y * row in garden:
        n += 1
    if x + (y + 1) * row in garden:
        n += 1
    if x + (y - 1) * row in garden:
        n += 1

    match n:
        case 0:
            return 4
        case 1:
            return 2
        case 2:
            return 0
        case 3:
            return -2
        case 4:
            return -4


def count_corners(garden: list[int]) -> int:
    corners = 0

    for i in garden:
        # check convex corners
        if i - 1 not in garden and i - row not in garden:
            corners += 1
        if i + 1 not in garden and i - row not in garden:
            corners += 1
        if i + 1 not in garden and i + row not in garden:
            corners += 1
        if i - 1 not in garden and i + row not in garden:
            corners += 1

        # check concave corners
        if i - 1 in garden and i - row in garden and i - 1 - row not in garden:
            corners += 1
        if i + 1 in garden and i - row in garden and i + 1 - row not in garden:
            corners += 1
        if i + 1 in garden and i + row in garden and i + 1 + row not in garden:
            corners += 1
        if i - 1 in garden and i + row in garden and i - 1 + row not in garden:
            corners += 1

    return corners


map = copy.deepcopy(data)
map = [list(item) for item in map]

price = 0
price2 = 0

for i in range(row):
    for j in range(col):
        if map[i][j] == ".":
            continue

        type = map[i][j]
        map[i][j] = "."
        garden = [i + j * row]
        index = 0
        perimeter = 4

        while index < len(garden):
            x = garden[index] % row
            y = int((garden[index] - x) / row)

            if x < row - 1 and map[x + 1][y] == type:
                map[x + 1][y] = "."
                perimeter += update_perimeter(x + 1 + y * row, garden)
                garden.append(x + 1 + y * row)
            if x > 0 and map[x - 1][y] == type:
                map[x - 1][y] = "."
                perimeter += update_perimeter(x - 1 + y * row, garden)
                garden.append(x - 1 + y * row)
            if y < col - 1 and map[x][y + 1] == type:
                map[x][y + 1] = "."
                perimeter += update_perimeter(x + (y + 1) * row, garden)
                garden.append(x + (y + 1) * row)
            if y > 0 and map[x][y - 1] == type:
                map[x][y - 1] = "."
                perimeter += update_perimeter(x + (y - 1) * row, garden)
                garden.append(x + (y - 1) * row)

            index += 1

        area = len(garden)
        side = count_corners(garden)

        # print(f"type: {type}, area: {area}, perimeter: {perimeter}, side: {side}")
        price += area * perimeter
        price2 += area * side


print(price)

# --- part 2 ---

print(price2)
