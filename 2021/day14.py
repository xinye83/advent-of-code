data = open("input/day14.in", "r").read().strip("\n").split("\n\n")
template = data[0]
pairs = [line.split(" -> ") for line in data[1].split("\n")]
pairs = {key: value for key, value in pairs}

polymer = template[:]
steps = 10

for _ in range(steps):
    index = 0

    while index < len(polymer):
        if polymer[index: index + 2] in pairs:
            polymer = (
                    polymer[: index + 1]
                    + pairs[polymer[index: index + 2]]
                    + polymer[index + 1:]
            )
            index += 1

        index += 1

visited = ""
maxval = 0
minval = len(polymer)

for c in polymer:
    if c not in visited:
        visited += c
        maxval = max(maxval, polymer.count(c))
        minval = min(minval, polymer.count(c))

print(f"Part 1 - {maxval - minval}")

polymer = template[:]
steps = 40

database = {}
count = {}


def count_occurrence(pair, step):
    global database
    global steps
    global pairs

    if pair not in database or database[pair][step] is None:
        if pair not in database:
            database[pair] = [None for _ in range(steps + 1)]

        if step == 0:
            if pair[0] == pair[1]:
                database[pair][step] = {pair[0]: 2}
            else:
                database[pair][step] = {pair[0]: 1, pair[1]: 1}
        else:
            if pair not in pairs:
                count_occurrence(pair, step - 1)
                database[pair][step] = database[pair][step - 1].copy()
            else:
                count_occurrence(pair[0] + pairs[pair], step - 1)
                count_occurrence(pairs[pair] + pair[1], step - 1)

                database[pair][step] = database[pair[0] + pairs[pair]][step - 1].copy()

                for key, value in database[pairs[pair] + pair[1]][step - 1].items():
                    if key in database[pair][step]:
                        database[pair][step][key] += value
                    else:
                        database[pair][step][key] = value

                database[pair][step][pairs[pair]] -= 1


for i in range(len(polymer) - 1):
    count_occurrence(polymer[i: i + 2], steps)
    for key, value in database[polymer[i: i + 2]][steps].items():
        if key not in count:
            count[key] = value
        else:
            count[key] += value

    if i != len(polymer) - 2:
        count[polymer[i + 1]] -= 1

print(f"Part 2 - {max(count.values()) - min(count.values())}")
