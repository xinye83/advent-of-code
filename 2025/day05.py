from pathlib import Path

ranges, ingredients = (
    Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n\n")
)

ranges = ranges.split("\n")
ingredients = ingredients.split("\n")

# --- part 1 ---

count = 0

for i in ingredients:
    i = int(i)
    fresh = False

    for r in ranges:
        l, h = r.split("-")
        if int(l) <= i and i <= int(h):
            fresh = True
            break

    if fresh:
        count += 1

print(count)

# --- part 2 ---

l = list()

for r in ranges:
    a, b = r.split("-")
    a = int(a)
    b = int(b)

    i = 0
    while i < len(l):
        if a <= l[i][1] + 1:
            break
        i += 1

    if i == len(l):
        l.append((a, b))
        continue

    if b < l[i][0] - 1:
        l.insert(i, (a, b))
        continue

    j = i
    while j < len(l):
        if b < l[j][0] - 1:
            break
        j += 1

    new = (min(a, l[i][0]), max(b, l[j - 1][1]))
    del l[i:j]
    l.insert(i, new)


count2 = sum([b - a + 1 for a, b in l])
print(count2)
