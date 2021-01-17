#--- Day 10: Adapter Array ---

data = []

with open('input/day_10.in', 'r') as file:
	data = [int(line) for line in file]

#--- part 1 ---

import copy

adapter = copy.deepcopy(data)
adapter.append(0)

adapter.sort()

count1 = 0
count3 = 0

for i in range(len(adapter)):
	if i == len(adapter) - 1 or adapter[i + 1] - adapter[i] == 3:
		count3 += 1
	elif adapter[i + 1] - adapter[i] == 1:
		count1 += 1

print(count1 * count3)

#--- part 2 ---

counter = [0] * len(adapter)
counter[0] = 1

for i in range(len(adapter)):

	for j in range(i + 1, len(adapter)):
		if adapter[j] - adapter[i] > 3:
			break

		counter[j] += counter[i]

print(counter[len(counter) - 1])
