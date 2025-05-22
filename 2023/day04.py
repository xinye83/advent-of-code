from util import *

data = get_input().split("\n")

# --- part 1 ---
point = 0

for card in data:
    win, have = card.split(":")[-1].split("|")
    win = [int(item) for item in win.split()]
    have = [int(item) for item in have.split()]

    point += int(pow(2, len(set(win) & set(have)) - 1))

print(point)

# --- part 2 ---
number = 0

card = [None] + [1 for _ in range(len(data))]

id = 0

for line in data:
    id += 1

    win, have = line.split(":")[-1].split("|")
    win = [int(item) for item in win.split()]
    have = [int(item) for item in have.split()]
    match = len(set(win) & set(have))

    for i in range(match):
        card[id + i + 1] += card[id]

print(sum(card[1:]))
