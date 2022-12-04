from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day04.in').read_text().split('\n')

# part 1
contain = 0

for line in data:
    first, second = line.split(',')

    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    if first[0] <= second[0] and first[1] >= second[1] or first[0] >= second[0] and first[1] <= second[1]:
        contain += 1

print(contain)

# part 2
overlap = 0
for line in data:
    first, second = line.split(',')

    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    if second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1] or \
            first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1]:
        overlap += 1

print(overlap)
