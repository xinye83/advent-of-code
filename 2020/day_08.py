data = []

with open('input/day_08.in', 'r') as file:
	for line in file:
		data.append([line[:3], int(line[3:])])

#--- part 1 ---

visited = [False] * len(data)
accumulator = 0
pos = 0

while True:
	if visited[pos]:
		break

	visited[pos] = True

	if data[pos][0] == 'acc':
		accumulator += data[pos][1]
		pos += 1
	elif data[pos][0] == 'jmp':
		pos += data[pos][1]
	else:
		pos += 1

print(accumulator)

#--- part 2 ---

import copy

for i in range(len(data)):
	if data[i][0] == 'acc':
		continue

	instr = copy.deepcopy(data)
	if instr[i][0] == 'jmp':
		instr[i][0] = 'nop'
	else:
		instr[i][0] = 'jmp'

	visited = [False] * len(instr)
	accumulator = 0
	pos = 0

	while True:
		# solution found
		if pos == len(instr):
			print(accumulator)
			exit(0)

		if visited[pos]:
			break

		visited[pos] = True

		if instr[pos][0] == 'acc':
			accumulator += instr[pos][1]
			pos += 1
		elif instr[pos][0] == 'jmp':
			pos += instr[pos][1]
		else:
			pos += 1
