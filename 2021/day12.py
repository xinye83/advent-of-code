data = open("input/day12.in", "r").read().strip("\n").split("\n")
paths = [line.split("-") for line in data]

connected = {}
for path in paths:
    if path[0] not in connected:
        connected[path[0]] = [path[1]]
    elif path[1] not in connected[path[0]]:
        connected[path[0]].append(path[1])

    if path[1] not in connected:
        connected[path[1]] = [path[0]]
    elif path[0] not in connected[path[1]]:
        connected[path[1]].append(path[0])


def is_small_cave(cave):
    for c in cave:
        if c.upper() == c:
            return False

    return True


stack = [["start"]]
total = 0

while len(stack) > 0:
    path = stack.pop(0)
    last = path[-1]

    for next in connected[last]:
        if next == "end":
            total += 1
            continue
        elif next == "start":
            continue

        if is_small_cave(next) and next in path:
            continue

        stack.append(path + [next])

print(f"Part 1 - {total}")

# first item store "the" small cave that's been visited twice in this path
stack = [[None, "start"]]
total = 0

while len(stack) > 0:
    path = stack.pop(0)
    last = path[-1]

    for next in connected[last]:
        if next == "end":
            total += 1
            continue
        elif next == "start":
            continue

        if is_small_cave(next):
            if next not in path:
                stack.append(path + [next])
            elif path[0] is not None:
                continue
            else:
                stack.append([next] + path[1:] + [next])
        else:
            stack.append(path + [next])

print(f"Part 2 - {total}")
