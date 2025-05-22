from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().replace("\n", "")


def mul(a, b):
    return a * b


# --- part 1 ---

import re

result = 0

match = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)

for item in match:
    result += eval(item)

print(result)

# --- part 2 ---

match = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data)

result = 0
do = True

for item in match:
    if item == "do()":
        do = True
    elif item == "don't()":
        do = False
    elif do:
        result += eval(item)

print(result)
