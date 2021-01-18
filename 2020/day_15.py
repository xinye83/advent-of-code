#--- Day 15: Rambunctious Recitation ---

data = [0, 13, 1, 16, 6, 17]

#--- part 1 ---

def my_num(last_spoken, last_num, start_turn, my_turn):

	for turn in range(start_turn, my_turn + 1):

		if last_spoken[last_num][0] == -1:
			last_num = 0
		else:
			last_num = last_spoken[last_num][1] - last_spoken[last_num][0]

		if last_num not in last_spoken:
			last_spoken[last_num] = [-1, turn]
		else:
			last_spoken[last_num][0] = last_spoken[last_num][1]
			last_spoken[last_num][1] = turn

	return last_num

print(my_num( \
	{
		0: [-1, 1],
		13: [-1, 2],
		1: [-1, 3],
		16: [-1, 4],
		6: [-1, 5],
		17: [-1, 6]
	}, \
	17, 7, 2020))

#--- part 2 ---

print(my_num( \
	{
		0: [-1, 1],
		13: [-1, 2],
		1: [-1, 3],
		16: [-1, 4],
		6: [-1, 5],
		17: [-1, 6]
	}, \
	17, 7, 30000000))
