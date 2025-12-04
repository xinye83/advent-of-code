from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

row = len(data)
col = len(data[0])

# --- part 1 ---


def count_neighbor(i, j) -> int:
    c = 0

    for ii in (i - 1, i, i + 1):
        for jj in (j - 1, j, j + 1):
            if ii == i and jj == j:
                continue
            if ii < 0 or ii >= row or jj < 0 or jj >= col:
                continue
            if data[ii][jj] == "@":
                c += 1

    return c


accessible = 0

for i in range(row):
    for j in range(col):
        if data[i][j] != "@":
            continue
        if count_neighbor(i, j) < 4:
            accessible += 1

print(accessible)


# --- part 2 ---

cache = [[-1 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        if data[i][j] != "@":
            continue
        cache[i][j] = count_neighbor(i, j)


def remove_roll(i, j):
    cache[i][j] = -1

    for ii in (i - 1, i, i + 1):
        for jj in (j - 1, j, j + 1):
            if ii == i and jj == j:
                continue
            if ii < 0 or ii >= row or jj < 0 or jj >= col:
                continue
            if cache[ii][jj] != -1:
                cache[ii][jj] -= 1


cont = True
removed = 0

while cont:
    cont = False
    for i in range(row):
        for j in range(col):
            if cache[i][j] == -1:
                continue
            if cache[i][j] < 4:
                cont = True
                removed += 1
                remove_roll(i, j)

print(removed)
