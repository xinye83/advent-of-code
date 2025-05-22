from pathlib import Path

data = (Path(__file__).parent / "day01.in").read_text().strip("\n").split("\n")

# --- part 1 ---

left = []
right = []

for line in data:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total_distance = sum([abs(l - r) for l, r in zip(left, right)])

print(total_distance)

# --- part 2 ---

appear = {}

for r in right:
    if r not in appear:
        appear[r] = 1
    else:
        appear[r] += 1

similarity = 0

for l in left:
    if l in appear:
        similarity += appear[l] * l

print(similarity)
