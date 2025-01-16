from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n\n")

# --- part 1 ---


rules = {}

for line in data[0].split("\n"):
    m, n = line.split("|")
    m = int(m)
    n = int(n)
    if m not in rules:
        rules[m] = [n]
    else:
        rules[m].append(n)


middle_page = 0
unorderred = []

for line in data[1].split("\n"):
    update = [int(i) for i in line.split(",")]
    order = True

    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[j] not in rules:
                continue
            if update[i] in rules[update[j]]:
                order = False
                break

        if not order:
            break

    if order:
        middle_page += update[int(len(update) / 2)]
    else:
        unorderred.append(update)

print(middle_page)

# --- part 2 ---
