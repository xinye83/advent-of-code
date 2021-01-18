#--- Day 16: Ticket Translation ---

data = open('input/day_16.in', 'r').read()

#--- part 1 ---

def string_to_interval(string):

	i = string.find('-')
	return [int(string[:i]), int(string[i + 1:])]

def is_valid_number(number, valid_ranges):

	valid = False

	for field in valid_ranges:
		if (number >= valid_ranges[field][0] and number <= valid_ranges[field][1]) or \
			(number >= valid_ranges[field][2] and number <= valid_ranges[field][3]):
			valid = True

	return valid

# parse valid range

valid_ranges = {}

for line in data[:data.find('\n\n')].split('\n'):

	i = line.find(':')
	j = line.find(' or ')

	valid_ranges[line[:i].strip()] = \
		string_to_interval(line[i + 1:j].strip()) + \
		string_to_interval(line[j + 4:].strip())

# parse nearby tickets

sum = 0

for ticket in data[data.find('nearby tickets:\n') + len('nearby tickets:\n'):].strip('\n').split('\n'):
	for num in ticket.split(','):
		if not is_valid_number(int(num), valid_ranges):
			sum += int(num)

print(sum)

#--- part 2 ---

def is_valid_ticket(ticket, valid_ranges):

	valid = True

	for number in ticket:
		if not is_valid_number(number, valid_ranges):
			valid = False
			break

	return valid

valid_tickets = data[data.find('your ticket:\n') + len('your ticket:\n'):].replace('\nnearby tickets:\n', '').strip('\n').split('\n')
valid_tickets = [[int(number) for number in ticket.split(',')] for ticket in valid_tickets]

i = 0
while i < len(valid_tickets):
	if not is_valid_ticket(valid_tickets[i], valid_ranges):
		del valid_tickets[i]
	else:
		i += 1

# valid_tickets[0] is your ticket

field_index = {field: [] for field in valid_ranges}

for i in range(len(valid_tickets[0])):
	for field in valid_ranges:

		valid = True

		# check if the i-th number is valid for the field
		for j in range(len(valid_tickets)):
			number = valid_tickets[j][i]

			if not (number >= valid_ranges[field][0] and number <= valid_ranges[field][1]) and \
				not(number >= valid_ranges[field][2] and number <= valid_ranges[field][3]):
				valid = False
				break

		if valid:
			field_index[field] += [i]

field_index = {field: index for (field, index) in sorted(field_index.items(), key = lambda item: len(item[1]))}

for field in field_index:

	field_index[field] = field_index[field][0]

	for field2 in field_index:
		if field != field2 and type(field_index[field2]) is list:
			field_index[field2].remove(field_index[field])

prod = 1

for field in field_index:
	if field[:9] == 'departure':
		prod *= valid_tickets[0][field_index[field]]

print(prod)
