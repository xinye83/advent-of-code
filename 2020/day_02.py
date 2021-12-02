# --- Day 2: Password Philosophy ---

data = []

with open("input/day_02.in", "r") as file:
    for line in file:
        data.append(line.strip().replace(":", "").replace("-", " ").split(" "))
        data[len(data) - 1][0] = int(data[len(data) - 1][0])
        data[len(data) - 1][1] = int(data[len(data) - 1][1])

# --- part 1 ---

count1 = 0

for low, high, key, password in data:
    num = 0
    for char in password:
        if char == key:
            num += 1

    if low <= num and num <= high:
        count1 += 1

print(count1)

# --- part 2 ---

count2 = 0

for pos1, pos2, key, password in data:
    if (password[pos1 - 1] == key and password[pos2 - 1] != key) or (
        password[pos1 - 1] != key and password[pos2 - 1] == key
    ):
        count2 += 1

print(count2)
