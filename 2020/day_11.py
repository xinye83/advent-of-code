#--- Day 11: Seating System ---

data = []

with open('input/day_11.in', 'r') as file:
	data = [line.strip('\n') for line in file]

#--- part 1 ---

import copy

def occupied_neighbor(map, i, j):

	count = 0

	for ii in [-1, 0, 1]:
		for jj in [-1, 0, 1]:
			if ii == 0 and jj == 0:
				continue

			if i + ii < 0 or i + ii >= len(map):
				continue

			if j + jj < 0 or j + jj >= len(map[0]):
				continue

			if map[i + ii][j + jj] == '#':
				count += 1

	return count

changed = True

current = copy.deepcopy(data)

while changed:
	changed = False

	next = [[' ' for i in range(len(current[0]))] for j in range(len(current))]

	for i in range(len(current)):
		for j in range(len(current[0])):

			if current[i][j] == '.':
				next[i][j] = '.'
			elif current[i][j] == 'L':
				if occupied_neighbor(current, i, j) == 0:
					next[i][j] = '#'
					changed = True
				else:
					next[i][j] = 'L'
			else:
				if occupied_neighbor(current, i, j) >= 4:
					next[i][j] = 'L'
					changed = True
				else:
					next[i][j] = '#'

	current = next

occupied = 0

for i in range(len(current)):
	for j in range(len(current[0])):
		if current[i][j] == '#':
			occupied += 1

print(occupied)

#--- part 2 ---

def occupied_in_sight(map, i, j):

	count = 0

	for ii in [-1, 0, 1]:
		for jj in [-1, 0, 1]:
			if ii == 0 and jj == 0:
				continue

			k = 0

			while True:
				k += 1

				if i + k * ii < 0 or i + k * ii >= len(map):
					break

				if j + k * jj < 0 or j + k * jj >= len(map[0]):
					break

				if map[i + k * ii][j + k * jj] == '#':
					count += 1
					break
				elif map[i + k * ii][j + k * jj] == 'L':
					break

	return count

changed = True

current = copy.deepcopy(data)

while changed:
	changed = False

	next = [[' ' for i in range(len(current[0]))] for j in range(len(current))]

	for i in range(len(current)):
		for j in range(len(current[0])):

			if current[i][j] == '.':
				next[i][j] = '.'
			elif current[i][j] == 'L':
				if occupied_in_sight(current, i, j) == 0:
					next[i][j] = '#'
					changed = True
				else:
					next[i][j] = 'L'
			else:
				if occupied_in_sight(current, i, j) >= 5:
					next[i][j] = 'L'
					changed = True
				else:
					next[i][j] = '#'

	current = next

occupied = 0

for i in range(len(current)):
	for j in range(len(current[0])):
		if current[i][j] == '#':
			occupied += 1

print(occupied)
