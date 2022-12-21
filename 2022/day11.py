import math
from copy import deepcopy
from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day11.in').read_text().strip('\n').split('\n\n')

stack = []
operation = []
div = []
t = []
f = []


def process_data(data: list[str]):
    for monkey in data:
        lines = monkey.split('\n')

        stack.append([int(item) for item in lines[1].split(': ')[1].split(', ')])
        operation.append(lines[2].split('=')[1].replace(' ',''))
        div.append(int(lines[3].split('by')[1]))
        t.append(int(lines[4].split('monkey')[1]))
        f.append(int(lines[5].split('monkey')[1]))


process_data(data)

monkeys = deepcopy(stack)
inspections = [0 for _ in monkeys]

round = 20

for _ in range(round):
    for i in range(len(monkeys)):
        inspections[i] += len(monkeys[i])

        for item in monkeys[i]:
            worry_level = eval(operation[i].replace('old', str(item))) // 3

            if worry_level % div[i] == 0:
                monkeys[t[i]].append(worry_level)
            else:
                monkeys[f[i]].append(worry_level)

        monkeys[i] = []

inspections.sort()
print(inspections[-2] * inspections[-1])

# part 2

monkeys = deepcopy(stack)
inspections = [0 for _ in monkeys]

DIVISOR = math.prod(div)

round = 10000

for _ in range(round):
    for i in range(len(monkeys)):
        inspections[i] += len(monkeys[i])

        for item in monkeys[i]:
            worry_level = eval(operation[i].replace('old', str(item))) % DIVISOR

            if worry_level % div[i] == 0:
                monkeys[t[i]].append(worry_level)
            else:
                monkeys[f[i]].append(worry_level)

        monkeys[i] = []

inspections.sort()
print(inspections[-2] * inspections[-1])
