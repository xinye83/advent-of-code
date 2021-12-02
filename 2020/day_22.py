# --- Day 22: Crab Combat ---

data = open("input/day_22.in", "r").read().strip("\n").split("\n\n")

# --- part 1 ---

import queue

player1 = queue.Queue()
player2 = queue.Queue()

for card in data[0].split("\n")[1:]:
    player1.put(int(card))

for card in data[1].split("\n")[1:]:
    player2.put(int(card))

while not player1.empty() and not player2.empty():
    card1 = player1.get()
    card2 = player2.get()

    if card1 > card2:
        player1.put(card1)
        player1.put(card2)
    else:
        player2.put(card2)
        player2.put(card1)

if not player1.empty():
    winner = player1
else:
    winner = player2

sum = 0
count = 0
score = 0

while not winner.empty():
    card = winner.get()

    sum += card
    count += 1
    score -= count * card

score += (count + 1) * sum

print(score)

# --- part 2 ---

# deck1 and deck2 are lists of cards in the each
# decks with the top card on the left of the list
def recursive_combat(deck1, deck2):

    history = []

    while len(deck1) > 0 and len(deck2) > 0:

        if deck1 + [0] + deck2 in history:
            return True, deck1, deck2
        else:
            history.append(deck1 + [0] + deck2)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            win = recursive_combat(deck1[:card1], deck2[:card2])[0]
        else:
            win = card1 > card2

        if win:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    if len(deck1) == 0:
        return False, deck1, deck2
    if len(deck2) == 0:
        return True, deck1, deck2


deck1 = [int(card) for card in data[0].split("\n")[1:]]
deck2 = [int(card) for card in data[1].split("\n")[1:]]

winner = recursive_combat(deck1, deck2)[0]

if winner:
    deck = deck1
else:
    deck = deck2

sum = 0
count = 0
score = 0

for card in deck:
    sum += card
    count += 1
    score -= count * card

score += (count + 1) * sum

print(score)
