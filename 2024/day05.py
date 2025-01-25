from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n\n")

# pages in rules[m] must be printed after page m
rules = {}

for line in data[0].split("\n"):
    m, n = line.split("|")
    m = int(m)
    n = int(n)
    if m not in rules:
        rules[m] = set()
        rules[m].add(n)
    else:
        rules[m].add(n)


# --- part 1 ---

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

middle_page_2 = 0

for line in unorderred:
    index = [0 for _ in line]

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[j] in rules[line[i]]:
                index[j] += 1
            else:
                index[i] += 1

    for i in range(len(line)):
        if index[i] == int(len(line) / 2):
            middle_page_2 += line[i]
            continue


print(middle_page_2)
