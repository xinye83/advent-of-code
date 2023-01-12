from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day15.in').read_text().strip('\n').split('\n')

for line in data:
