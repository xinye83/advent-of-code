from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n\n")

SHAPE = list()
REGION = list()

for item in data:
    item = item.split("\n")
    if item[0][-1] == ":":
        SHAPE.append(item[1:])
    else:
        for i in item:
            a, b = i.split(":")
            REGION.append([list(map(int, a.split("x"))), list(map(int, b.split()))])

# --- part 1 ---

# calculate areas

num = 0

for r in REGION:
    if r[0][0] * r[0][1] >= 9 * sum(r[1]):
        num += 1

print(num)
