# --- Day 7: Handy Haversacks ---

data = {}

with open("input/day_07.in", "r") as file:
    for line in file:
        i = line.find("contain")

        temp1 = line[:i].replace("bags", "").strip()
        temp2 = (
            line[i + len("contain") :]
            .replace("bags", "")
            .replace("bag", "")
            .strip(".\n")
            .split(",")
        )

        data[temp1] = {}

        for item in temp2:
            item = item.strip()

            if item == "no other":
                break

            j = item.find(" ")

            data[temp1][item[j:].strip()] = int(item[:j])

counter = 0

for bag in data:
    data[bag]["index"] = counter
    counter += 1

# --- part 1 ---

from collections import deque

# construct an "transition matrix"
# T[i][j] <== how many type j bags can a type i bag contain
T = [[0 for i in range(len(data))] for j in range(len(data))]

for i in data:
    for j in data[i]:
        if j != "index":
            T[data[i]["index"]][data[j]["index"]] = data[i][j]

contain = [False] * len(data)

q = deque()
q.append(data["shiny gold"]["index"])

while len(q) > 0:
    i = q.popleft()

    if contain[i]:
        continue

    contain[i] = True

    for j in range(len(data)):

        if T[j][i] > 0:
            q.append(j)

# the array contain will also mark 'shiny gold' as True
print(sum(contain) - 1)

# --- part 2 ---


def num_of_bags(bag):
    count = 0

    for item in data[bag]:
        if item != "index":
            count += data[bag][item] * (1 + num_of_bags(item))

    return count


print(num_of_bags("shiny gold"))
