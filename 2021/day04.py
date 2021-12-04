from aoc21 import *

data = read_paragraph("input/day04.in")

# size of the board
size = 5

drawn = list(map(int, data[0].split(",")))
boards = []
for board in data[1:]:
    boards.append([list(map(int, row.split())) for row in board.split("\n")])


def get_winning_info(drawn, board):
    turn = 0
    total = sum([sum(row) for row in board])

    rows = [0 for i in range(size)]
    cols = [0 for i in range(size)]

    for num in drawn:
        for i, j in itertools.product(range(5), range(5)):
            if board[i][j] == num:
                total -= num
                rows[i] += 1
                cols[j] += 1

                if rows[i] == 5 or cols[j] == 5:
                    return turn, total * num

        turn += 1

    return turn, -1


turn = len(drawn)
value = -1

for board in boards:
    i, j = get_winning_info(drawn, board)

    if i < turn:
        turn = i
        value = j

assert turn < len(drawn)

print(f"Part 1 - {value}")

turn = -1
value = -1

for board in boards:
    i, j = get_winning_info(drawn, board)

    if i > turn:
        turn = i
        value = j

assert turn < len(drawn)

print(f"Part 2 - {value}")
