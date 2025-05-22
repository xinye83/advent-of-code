from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---

map = dict()

for c in data:
    a, b = c.split("-")

    if a not in map:
        map[a] = set()
    if b not in map:
        map[b] = set()

    map[a].add(b)
    map[b].add(a)

interconnect = set()

for c1 in map:
    for c2 in map[c1]:
        for c3 in map[c1]:
            if c2 == c3:
                continue
            if c2 not in map[c3]:
                continue
            if "t" not in c1[0] + c2[0] + c3[0]:
                continue
            t = [c1, c2, c3]
            t.sort()
            interconnect.add(tuple(t))

print(len(interconnect))

# --- part 2 ---

visited = set()
parties = list()

for key in map:
    if key in visited:
        continue

    party = [key]
    visited.add(key)

    for next in map[key]:
        if next in visited:
            continue
        valid = True
        for prev in party:
            if prev not in map[next]:
                valid = False
                break
        if valid:
            party.append(next)
            visited.add(next)

    party.sort()
    parties.append(tuple(party))

parties.sort(key=lambda s: len(s))

print(",".join(parties[-1]))
