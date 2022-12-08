from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day06.in').read_text().strip('\n')

num = 4

while num <= len(data):
    if len(set(list(data[num - 4: num]))) == 4:
        break
    num += 1

print(num)

# part 2

num = 14

counter = {}
for c in data[:num]:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1

while num < len(data):
    if data[num] in counter:
        counter[data[num]] += 1
    else:
        counter[data[num]] = 1

    counter[data[num - 14]] -= 1
    if counter[data[num - 14]] == 0:
        del counter[data[num - 14]]

    num += 1

    if len(counter) == 14:
        break

print(num)
