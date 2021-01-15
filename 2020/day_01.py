data = []

with open('input/day_01.in', 'r') as file:
	for line in file:
		data.append(int(line))

sum = 2020

# part 1

temp1 = []

for i in data:
	if i in temp1:
		print(i * (sum - i))
		break
	else:
		temp1.append(sum - i)

# part 2

temp2 = data
temp2.sort()

for i in range(len(temp2) - 2):
	l = i + 1
	r = len(temp2) - 1

	while (l < r):
		if temp2[i] + temp2[l] + temp2[r] == sum:
			print(temp2[i] * temp2[l] * temp2[r])
			break
		elif temp2[i] + temp2[l] + temp2[r] < sum:
			l += 1
		else:
			r -= 1
