import re
from util import *

data = get_input()

# --- part 1 ---
value = 0

for item in data.split("\n"):
    match = re.findall(r"\d", item, re.A)
    value += int(match[0] + match[-1])

print(value)

# --- part 2 ---
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

value = 0

for item in data.split("\n"):
    match = re.findall(r"(?=(\d|" + "|".join(key for key in digits) + "))", item, re.A)

    temp = ""
    if match[0] in digits:
        temp += digits[match[0]]
    else:
        temp += match[0]
    if match[-1] in digits:
        temp += digits[match[-1]]
    else:
        temp += match[-1]

    value += int(temp)

print(value)
