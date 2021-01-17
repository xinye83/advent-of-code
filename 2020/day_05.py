#--- Day 5: Binary Boarding ---

data = []

with open('input/day_05.in', 'r') as file:
	for line in file:
		data.append(line.strip('\n'))

def seatID(seat):

	row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
	col = int(seat[7:].replace('R', '1').replace('L', '0'), 2)

	return row * 8 + col

#--- part 1 ---

maxval = 0

for seat in data:
	maxval = max(maxval, seatID(seat))

print(maxval)

#--- part 2 ---

maxID = 127 * 8 + 7

taken = [False] * (maxID + 1)

for seat in data:
	taken[seatID(seat)] = True

for id in range(1, len(taken)-1):
	if not taken[id] and taken[id - 1] and taken[id + 1]:
		break

print(id)
