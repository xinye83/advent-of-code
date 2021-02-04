#--- Day 24: Lobby Layout ---

data = open('input/day_24.in', 'r').read().strip('\n').split('\n')

#--- part 1 ---

# e ==> x + 1
# w ==> x - 1
# ne ==> x + 1 & y + 1
# sw ==> x - 1 & y - 1
# nw ==> y + 1
# se ==> y - 1

flipped = []

for tile in data:
	cood = [0, 0]
	i = 0

	while i < len(tile):
		if tile[i] == 'e':
			cood[0] += 1
			i += 1
		elif tile[i] == 'w':
			cood[0] -= 1
			i += 1
		elif tile[i:i + 2] == 'ne':
			cood[0] += 1
			cood[1] += 1
			i += 2
		elif tile[i:i + 2] == 'sw':
			cood[0] -= 1
			cood[1] -= 1
			i += 2
		elif tile[i:i + 2] == 'nw':
			cood[1] += 1
			i += 2
		elif tile[i:i + 2] == 'se':
			cood[1] -= 1
			i += 2

	if cood in flipped:
		flipped.remove(cood)
	else:
		flipped.append(cood)

print(len(flipped))

#--- part 2 ---

def day(tiles, x1, x2, y1, y2):
	result = []

	for x in range(x1 - 1, x2 + 2):
		for y in range(y1 - 1, y2 + 2):
			n = 0

			if [x + 1, y] in tiles:
				n += 1
			if [x - 1, y] in tiles:
				n += 1
			if [x, y + 1] in tiles:
				n += 1
			if [x, y - 1] in tiles:
				n += 1
			if [x + 1, y + 1] in tiles:
				n += 1
			if [x - 1, y - 1] in tiles:
				n += 1

			if ([x, y] in tiles and (n == 1 or n == 2)) or \
				([x, y] not in tiles and n == 2):
				result.append([x, y])
				x1 = min(x1, x)
				x2 = max(x2, x)
				y1 = min(y1, y)
				y2 = max(y2, y)

	return result, x1, x2, y1, y2

x1 = flipped[0][0]
x2 = flipped[0][0]
y1 = flipped[0][1]
y2 = flipped[0][1]

for [x, y] in flipped:
	x1 = min(x1, x)
	x2 = max(x2, x)
	y1 = min(y1, y)
	y2 = max(y2, y)

for i in range(100):
	flipped, x1, x2, y1, y2 = day(flipped, x1, x2, y1, y2)

print(len(flipped))
