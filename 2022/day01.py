from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day01.in').read_text().split('\n')

# part 1
max_cal = 0
cur_cal = 0

for line in data:
    if line == '':
        max_cal = max(max_cal, cur_cal)
        cur_cal = 0
    else:
        cur_cal += int(line)

print(max_cal)

# part 2
max_cal = []
cur_cal = 0

for line in data:
    if line == '':
        max_cal.append(cur_cal)
        cur_cal = 0
    else:
        cur_cal += int(line)

max_cal.sort(reverse=True)
print(sum(max_cal[:3]))
