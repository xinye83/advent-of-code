import re
from util import *

data = get_input()

# --- part 1 ---
cube = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

value = 0

for item in data.split("\n"):
    match = re.match("Game \d+:", item)
    id = int(match[0].replace("Game ", "").replace(":", ""))

    valid = True
    for set in item.split(":")[-1].split(";"):
        for c in set.split(","):
            number, color = c.strip().rstrip().split(" ")
            if cube[color] < int(number):
                valid = False
                break
        if not valid:
            break

    if valid:
        value += id

print(value)

# --- part 2 ---

power = 0

for item in data.split("\n"):

    cube = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for set in item.split(":")[-1].split(";"):
        for c in set.split(","):
            number, color = c.strip().rstrip().split(" ")
            cube[color] = max(cube[color], int(number))

    power += cube["red"] * cube["blue"] * cube["green"]

print(power)
