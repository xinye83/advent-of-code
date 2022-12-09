from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day08.in').read_text().strip('\n').split('\n')

trees = []
for line in data:
    trees.append([int(i) for i in list(line)])

row = len(trees)
col = len(trees[0])

visible = [[False for _ in range(col)] for _ in range(row)]

for i in range(row):
    cur = -1
    for j in range(col):
        visible[i][j] |= trees[i][j] > cur
        cur = max(cur, trees[i][j])

    cur = -1
    for j in reversed(range(col)):
        visible[i][j] |= trees[i][j] > cur
        cur = max(cur, trees[i][j])

for j in range(col):
    cur = -1
    for i in range(row):
        visible[i][j] |= trees[i][j] > cur
        cur = max(cur, trees[i][j])

    cur = -1
    for i in reversed(range(row)):
        visible[i][j] |= trees[i][j] > cur
        cur = max(cur, trees[i][j])

num = 0
for i in range(row):
    for j in range(col):
        if visible[i][j]:
            num += 1

print(num)

# part 2

score = 0

for i in range(row):
    if i == 0 or i == row - 1:
        continue
    for j in range(col):
        if j == 0 or j == col - 1:
            continue

        temp = 1

        k = 1
        while True:
            if trees[i - k][j] >= trees[i][j] or i - k == 0:
                break
            k += 1
        temp *= k

        k = 1
        while True:
            if trees[i + k][j] >= trees[i][j] or i + k == row - 1:
                break
            k += 1
        temp *= k

        k = 1
        while True:
            if trees[i][j - k] >= trees[i][j] or j - k == 0:
                break
            k += 1
        temp *= k

        k = 1
        while True:
            if trees[i][j + k] >= trees[i][j] or j + k == col - 1:
                break
            k += 1
        temp *= k

        score = max(score, temp)

print(score)
