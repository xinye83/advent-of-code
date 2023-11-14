# --- Day 19: Monster Messages ---

temp, messages = open("input/day_19.in", "r").read().split("\n\n")
messages = messages.strip("\n").split("\n")


class Rule:
    def __init__(self, rule):
        self.rule = rule.split("|")
        self.rule = [i.strip().split() for i in self.rule]

        for i in range(len(self.rule)):
            for j in range(len(self.rule[i])):
                if '"' in self.rule[i][j]:
                    self.rule[i][j] = self.rule[i][j].replace('"', "")
                else:
                    self.rule[i][j] = int(self.rule[i][j])


temp = temp.strip("\n").split("\n")

rules = {}
for item in temp:
    i = item.find(":")
    rules[int(item[:i].strip())] = Rule(item[i + 1:].strip())


def is_valid(message, start, key, rules):
    if start >= len(message):
        return False, -1

    if (
            len(rules[key].rule) == 1
            and len(rules[key].rule[0]) == 1
            and rules[key].rule[0][0] in ["a", "b"]
    ):
        return message[start] == rules[key].rule[0][0], start + 1

    for i in range(len(rules[key].rule)):

        temp = True
        start0 = start

        for j in range(len(rules[key].rule[i])):
            result = is_valid(message, start0, rules[key].rule[i][j], rules)
            temp = temp and result[0]
            start0 = result[1]

            if not temp:
                break

        if temp:
            return True, start0

    return False, -1


# --- part 1 ---

count = 0
for message in messages:
    result = is_valid(message, 0, 0, rules)
    if result[0] and result[1] == len(message):
        count += 1

print(count)

# --- part 2 ---

rules[8].rule = [[42], [42, 8]]
rules[11].rule = [[42, 31], [42, 11, 31]]

count = 0
for message in messages:
    result = is_valid(message, 0, 0, rules)
    if result[0] and result[1] == len(message):
        count += 1

print(count)
