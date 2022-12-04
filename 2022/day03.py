import string
from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day03.in').read_text().split('\n')

priorities = {letter: string.ascii_lowercase.index(letter) + 1 for letter in string.ascii_lowercase} | {
    letter: string.ascii_uppercase.index(letter) + 27 for letter in string.ascii_uppercase}

# part 1
misplace = 0

for line in data:
    first_half = set(list(line[:int(len(line) / 2)]))
    second_half = set(list(line[int(len(line) / 2):]))

    misplace += priorities[list(first_half.intersection(second_half))[0]]

print(misplace)

# part 2
misplace = 0

for i, j, k in zip(data[0::3], data[1::3], data[2::3]):
    misplace += priorities[list(set(list(i)).intersection(set(list(j)), set(list(k))))[0]]

print(misplace)
