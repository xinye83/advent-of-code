#--- Day 20: Jurassic Jigsaw ---

data = open('input/day_20.in', 'r').read().strip('\n').split('\n\n')

class Image():

	def __init__(self, grid, neighbor):
		self.grid = grid
		self.neighbor = neighbor

camera = {}

for item in data:
	j = item.find('\n')

	id = int(item[5:j - 1])
	image = item[j + 1:].split('\n')

	camera[id] = Image(image, 0)

#--- part 1 ---

edges = {}

for id in camera:

	top = camera[id].grid[0]
	bottom = camera[id].grid[-1]

	left = ''
	right = ''
	for line in camera[id].grid:
		left += line[0]
		right += line[-1]

	for edge, side in zip([top, bottom, left, right], [0, 1, 2, 3]):
		if edge not in edges and edge[::-1] not in edges:
			edges[edge] = [[id, side, 0]]
		elif edge in edges:
			edges[edge].append([id, side, 0])
		else:
			edges[edge[::-1]].append([id, side, 1]) # 1 ==> reverse

for edge in edges:
	if len(edges[edge]) == 2:
		camera[edges[edge][0][0]].neighbor += 1
		camera[edges[edge][1][0]].neighbor += 1

prod = 1
for id in camera:
	if camera[id].neighbor == 2:
		prod *= id

print(prod)
