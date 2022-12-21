from pathlib import Path

file = (Path.cwd() / 'input' / 'day10.in').open()

sum_signal = 0
x = 1
cycle = 1
cache = None

while cycle <= 220:
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum_signal += x * cycle

    cycle += 1

    if cache is None:
        line = file.readline()
        line = line.strip('\n')

        if line == 'noop':
            continue
        else:
            cache = int(line.split()[1])
    else:
        x += cache
        cache = None

file.close()

print(sum_signal)

# part 2
row = 6
col = 40
panel = [['.' for _ in range(col)] for _ in range(row)]

file = (Path.cwd() / 'input' / 'day10.in').open()

x = 1
cycle = 1
cache = None

while cycle <= row * col:
    pixel = (cycle - 1) % 40
    if pixel in [x - 1, x, x + 1]:
        panel[(cycle - 1) // col][(cycle - 1) % col] = '#'

    cycle += 1

    if cache is None:
        line = file.readline()
        line = line.strip('\n')

        if line == 'noop':
            continue
        else:
            cache = int(line.split()[1])
    else:
        x += cache
        cache = None

file.close()

print('\n'.join(''.join(row) for row in panel))
