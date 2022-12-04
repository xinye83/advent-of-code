from enum import IntEnum
from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day02.in').read_text().split('\n')


# part 1
class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


opponent = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS
}

you = {
    'X': Shape.ROCK,
    'Y': Shape.PAPER,
    'Z': Shape.SCISSORS
}

score = 0

for line in data:
    a = opponent[line[0]]
    b = you[line[-1]]

    score += b

    if a == b:
        score += 3
    elif a == Shape.ROCK and b == Shape.PAPER or a == Shape.PAPER and b == Shape.SCISSORS or \
            a == Shape.SCISSORS and b == Shape.ROCK:
        score += 6

print(score)

# part 2
score = 0

for line in data:
    a = opponent[line[0]]

    if line[-1] == 'X':
        if a == Shape.ROCK:
            score += Shape.SCISSORS
        elif a == Shape.PAPER:
            score += Shape.ROCK
        else:
            score += Shape.PAPER
    elif line[-1] == 'Y':
        score += 3 + a
    else:  # 'Z'
        score += 6
        if a == Shape.ROCK:
            score += Shape.PAPER
        elif a == Shape.PAPER:
            score += Shape.SCISSORS
        else:
            score += Shape.ROCK

print(score)
