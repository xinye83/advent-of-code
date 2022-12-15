from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day10.in').read_text().strip('\n').split('\n')

sum_signal = 0
x = 1
cycle = 1
ops = {1: [], 2: []}

for line in data:
    for op in ops[1]:
        if op ==