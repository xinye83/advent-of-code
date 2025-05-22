from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n\n")
)

locks = []
keys = []

for item in data:
    item = item.split("\n")

    row = len(item)
    col = len(item[0])

    is_lock = item[0] == "#" * col

    height = [0] * col

    for r in item[1:-1]:
        for i in range(col):
            if r[i] == "#":
                height[i] += 1

    if is_lock:
        locks.append(tuple(height))
    else:
        keys.append(tuple(height))

row -= 2

pair = 0

for lock in locks:
    for key in keys:
        fit = True
        for i in range(col):
            if lock[i] + key[i] > row:
                fit = False
                break
        if fit:
            pair += 1

print(pair)
