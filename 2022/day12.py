from copy import deepcopy
from pathlib import Path

letter = 'abcdefghijklmnopqrstuvwxyz'

data = (Path(__file__).parent / 'input' / 'day12.in').read_text().strip('\n').split('\n')

grid = deepcopy(data)

row = len(grid)
col = len(grid[0])

start = [-1, -1]

for i in range(row):
    try:
        start[1] = grid[i].index('S')
    except ValueError:
        continue

    start[0] = i
    break

step = [[-1 for _ in range(col)] for _ in range(row)]
step[start[0]][start[1]] = 0
stack = [start]

while len(stack) > 0:
    i, j = stack.pop(0)
    if grid[i][j] == 'E':
        break

    a = grid[i][j]
    if a == 'S':
        a = 'a'

    cur = letter.index(a)

    if i - 1 >= 0:
        b = grid[i - 1][j]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) <= cur + 1 and (step[i-1][j] == -1 or step[i-1][j] > step[i][j] + 1):
            step[i-1][j] = step[i][j] + 1
            stack.append([i-1, j])
    if i + 1 < row:
        b = grid[i + 1][j]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) <= cur + 1 and (step[i+1][j] == -1 or step[i+1][j] > step[i][j] + 1):
            step[i+1][j] = step[i][j] + 1
            stack.append([i+1, j])
    if j - 1 >= 0:
        b = grid[i][j-1]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) <= cur + 1 and (step[i][j-1] == -1 or step[i][j-1] > step[i][j] + 1):
            step[i][j-1] = step[i][j] + 1
            stack.append([i, j-1])
    if j + 1 < col:
        b = grid[i][j+1]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) <= cur + 1 and (step[i][j+1] == -1 or step[i][j+1] > step[i][j] + 1):
            step[i][j+1] = step[i][j] + 1
            stack.append([i, j+1])

print(step[i][j])

# part 2

grid = deepcopy(data)

row = len(grid)
col = len(grid[0])

start = [-1, -1]

for i in range(row):
    try:
        start[1] = grid[i].index('E')
    except ValueError:
        continue

    start[0] = i
    break

step = [[-1 for _ in range(col)] for _ in range(row)]
step[start[0]][start[1]] = 0
stack = [start]

while len(stack) > 0:
    i, j = stack.pop(0)
    if grid[i][j] == 'a' or grid[i][j] == 'S':
        break

    a = grid[i][j]
    if a == 'E':
        a = 'z'

    cur = letter.index(a)

    if i - 1 >= 0:
        b = grid[i - 1][j]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) >= cur - 1 and (step[i-1][j] == -1 or step[i-1][j] > step[i][j] + 1):
            step[i-1][j] = step[i][j] + 1
            stack.append([i-1, j])
    if i + 1 < row:
        b = grid[i + 1][j]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) >= cur - 1 and (step[i+1][j] == -1 or step[i+1][j] > step[i][j] + 1):
            step[i+1][j] = step[i][j] + 1
            stack.append([i+1, j])
    if j - 1 >= 0:
        b = grid[i][j-1]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) >= cur - 1 and (step[i][j-1] == -1 or step[i][j-1] > step[i][j] + 1):
            step[i][j-1] = step[i][j] + 1
            stack.append([i, j-1])
    if j + 1 < col:
        b = grid[i][j+1]
        if b == 'S':
            b = 'a'
        if b == 'E':
            b = 'z'
        if letter.index(b) >= cur - 1 and (step[i][j+1] == -1 or step[i][j+1] > step[i][j] + 1):
            step[i][j+1] = step[i][j] + 1
            stack.append([i, j+1])

print(step[i][j])
