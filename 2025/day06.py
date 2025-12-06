from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

# --- part 1 ---

results = []
ops = []

for line in data[::-1]:
    line = line.split()
    for i in range(len(line)):
        if line[i] == "*":
            ops.append(line[i])
            results.append(1)
        elif line[i] == "+":
            ops.append(line[i])
            results.append(0)
        else:
            if ops[i] == "*":
                results[i] *= int(line[i])
            elif ops[i] == "+":
                results[i] += int(line[i])

print(sum(results))

# --- part 2 ---

results2 = []
ops2 = []

i = 0
while i < len(data[-1]):
    j = i + 1
    while j < len(data[-1]) and data[-1][j] == " ":
        j += 1

    # (op, start, length)
    if j == len(data[-1]):
        ops2.append((data[-1][i], i, j - i))
    else:
        ops2.append((data[-1][i], i, j - i - 1))

    if data[-1][i] == "*":
        results2.append(1)
    if data[-1][i] == "+":
        results2.append(0)

    i = j

for i in range(len(ops2)):
    op, start, length = ops2[i]
    for j in range(start, start + length):
        num = "".join([line[j] for line in data[:-1]])
        if op == "*":
            results2[i] *= int(num)
        elif op == "+":
            results2[i] += int(num)

print(sum(results2))
