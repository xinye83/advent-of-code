from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day09.in').read_text().strip('\n').split('\n')


def sign(integer):
    if integer > 0:
        return 1
    if integer < 0:
        return -1
    return 0


def update_tail(head_, tail_):
    if abs(head_[0] - tail_[0]) <= 1 and abs(head_[1] - tail_[1]) <= 1:
        return tail_[0], tail_[1]

    if min(abs(head_[0] - tail_[0]), abs(head_[1] - tail_[1])) == 0:
        return tail_[0] + int((head_[0] - tail_[0]) / 2), tail_[1] + int((head_[1] - tail_[1]) / 2)

    return tail_[0] + sign(head_[0] - tail_[0]), tail_[1] + sign(head_[1] - tail_[1])


head = [0, 0]
tail = [0, 0]

visited = set()
visited.add(tuple(tail))

for line in data:
    direction, length = line.split()
    length = int(length)

    for _ in range(length):
        if direction == 'R':
            head[0] += 1
        elif direction == 'L':
            head[0] -= 1
        elif direction == 'U':
            head[1] += 1
        elif direction == 'D':
            head[1] -= 1
        tail = update_tail(head, tail)
        visited.add(tuple(tail))

print(len(visited))

# part 2

knots = [[0, 0] for _ in range(10)]

visited = set()
visited.add(tuple(knots[-1]))

for line in data:
    direction, length = line.split()
    length = int(length)

    for _ in range(length):
        if direction == 'R':
            knots[0][0] += 1
        elif direction == 'L':
            knots[0][0] -= 1
        elif direction == 'U':
            knots[0][1] += 1
        elif direction == 'D':
            knots[0][1] -= 1

        for i in range(9):
            knots[i + 1] = list(update_tail(knots[i], knots[i + 1]))

        visited.add(tuple(knots[-1]))

print(len(visited))
