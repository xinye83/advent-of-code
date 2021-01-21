#--- Day 19: Monster Messages ---

temp, messages = open('input/day_19.in', 'r').read().split('\n\n')
messages = messages.strip('\n').split('\n')

class Rule:

	def __init__(self, rule):
		self.rule = rule.split('|')
		self.rule = [i.strip().split() for i in self.rule]

		for i in range(len(self.rule)):
			for j in range(len(self.rule[i])):
				if '"' in self.rule[i][j]:
					self.rule[i][j] = self.rule[i][j].replace('"', '')
				else:
					self.rule[i][j] = int(self.rule[i][j])

		if len(self.rule) == 1 and len(self.rule[0]) == 1 and \
			type(self.rule[0][0]) is not int:
			self.length = 1
		else:
			self.length = 0

	def __len__(self):
		return self.length

temp = temp.strip('\n').split('\n')

rules = {}
for item in temp:
	i = item.find(':')
	rules[int(item[:i].strip())] = Rule(item[i+1:].strip())

#--- part 1 ---

import itertools

def rule_length(key, rules):
	if len(rules[key]) > 0:
		# already calculated
		return len(rules[key])
	elif len(rules[key].rule[0]) == 1:
		return rule_length(rules[key].rule[0][0], rules)
	else:
		return rule_length(rules[key].rule[0][0], rules) + rule_length(rules[key].rule[0][1], rules)

def is_valid(message, key, rules):
	if len(message) != len(rules[key]):
		return False

	if len(rules[key].rule) == 1:
		if len(rules[key].rule[0]) == 1:
			if type(rules[key].rule[0][0]) is not int:
				return message[0] == rules[key].rule[0][0]
			else:
				return is_valid(message, rules[key].rule[0][0], rules)
		else:
			return is_valid(message[:len(rules[rules[key].rule[0][0]])], rules[key].rule[0][0], rules) and \
				is_valid(message[len(rules[rules[key].rule[0][0]]):], rules[key].rule[0][1], rules)
	else:
		if len(rules[key].rule[0]) == 1:
			if type(rules[key].rule[0][0]) is not int:
				valid1 = message[0] == rules[key].rule[0][0]
			else:
				valid1 = is_valid(message, rules[key].rule[0][0], rules)
		else:
			valid1 = is_valid(message[:len(rules[rules[key].rule[0][0]])], rules[key].rule[0][0], rules) and \
				is_valid(message[len(rules[rules[key].rule[0][0]]):], rules[key].rule[0][1], rules)

		if len(rules[key].rule[1]) == 1:
			if type(rules[key].rule[1][0]) is not int:
				valid2 = message[0] == rules[key].rule[1][0]
			else:
				valid2 = is_valid(message, rules[key].rule[1][0], rules)
		else:
			valid2 = is_valid(message[:len(rules[rules[key].rule[1][0]])], rules[key].rule[1][0], rules) and \
				is_valid(message[len(rules[rules[key].rule[1][0]]):], rules[key].rule[1][1], rules)

		return valid1 or valid2

# calulate the length of each rules
for key in rules:
	rules[key].length = rule_length(key, rules)

count = 0
for message in messages:
	if is_valid(message, 0, rules):
		count += 1

print(count)

#--- part 2 ---
