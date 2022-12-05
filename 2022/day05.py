from pathlib import Path

starting, steps = (Path(__file__).parent / 'input' / 'day05.in').read_text().split('\n\n')

starting = starting.split('\n')
steps = steps.split('\n')


def init_stack(_starting):
    _stacks = {int(i): [] for i in _starting[-1].split()}
    for level in reversed(_starting[:-1]):
        for i in _stacks:
            crate = level[(i - 1) * 4 + 1]
            if crate == ' ':
                continue

            _stacks[i].append(crate)

    return _stacks


# part 1

stacks = init_stack(starting)

for step in steps:
    _, number, _, start, _, end = step.split()
    number = int(number)
    start = int(start)
    end = int(end)

    stacks[end].extend(reversed(stacks[start][-number:]))
    del stacks[start][-number:]

print(''.join(stacks[i][-1] for i in stacks))

# part 2

stacks = init_stack(starting)

for step in steps:
    _, number, _, start, _, end = step.split()
    number = int(number)
    start = int(start)
    end = int(end)

    stacks[end].extend(stacks[start][-number:])
    del stacks[start][-number:]

print(''.join(stacks[i][-1] for i in stacks))
