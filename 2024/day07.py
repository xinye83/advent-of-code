from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---


def is_valid(left, right):
    left = int(left)
    right = [int(item) for item in right.split(" ")]

    result = []

    for i in right:
        if not result:
            result = [i]
            continue

        new = []

        for j in result:
            new.append(j + i)
            new.append(j * i)

        result = new

    return left in result


sum = 0

for line in data:
    left, right = line.split(":")
    if is_valid(left.strip(), right.strip()):
        sum += int(left)

print(sum)

# --- part 2 ---


def is_valid_2(left, right):
    left = int(left)
    right = [int(item) for item in right.split(" ")]

    result = []

    for i in right:
        if not result:
            result = [i]
            continue

        new = []

        for j in result:
            new.append(j + i)
            new.append(j * i)
            new.append(int(str(j) + str(i)))

        result = new

    return left in result


sum = 0

for line in data:
    left, right = line.split(":")
    if is_valid_2(left.strip(), right.strip()):
        sum += int(left)

print(sum)
