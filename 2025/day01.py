from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n")

# --- part 1 ---

position = 50
password = 0

for item in data.split("\n"):
    dir = item[0]
    num = int(item[1:])

    if dir == "L":
        position -= num
    else:
        position += num

    position %= 100

    if position == 0:
        password += 1

print(password)

# --- part 2 ---

position = 50
password2 = 0

for item in data.split("\n"):
    dir = item[0]
    num = int(item[1:])

    temp = 1 if dir == "L" and position == 0 else 0

    if dir == "L":
        position -= num
    else:
        position += num

    if position >= 100:
        password2 += int(position / 100)
    elif position <= 0:
        password2 += int((100 - position) / 100)

    password2 -= temp
    position %= 100

print(password2)
