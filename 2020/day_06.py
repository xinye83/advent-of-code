# --- Day 6: Custom Customs ---

data = []

with open("input/day_06.in", "r") as file:
    temp = file.read().strip("\n").split("\n\n")

    for group in temp:
        data.append(group.split("\n"))

# --- part 1 ---

count = 0

for group in data:
    yes = [False] * 26

    for person in group:
        for ans in person:
            yes[ord(ans) - ord("a")] = True

    count += sum(yes)

print(count)

# --- part 2 ---

count = 0

for group in data:
    yes = [len(group)] * 26

    for person in group:
        for ans in person:
            yes[ord(ans) - ord("a")] -= 1

    for c in yes:
        if c == 0:
            count += 1

print(count)
