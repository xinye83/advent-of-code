from aoc21 import *

chunks = open("input/day10.in", "r").read().strip("\n").split("\n")
incomplete = []

illegal = [0, 0, 0, 0]

for chunk in chunks:

    temp = [[], [], [], []]
    skip = False

    for i, c in enumerate(chunk):
        if c == "(":
            temp[0].append(i)
        elif c == "[":
            temp[1].append(i)
        elif c == "{":
            temp[2].append(i)
        elif c == "<":
            temp[3].append(i)
        elif c == ")":
            if (
                len(temp[0]) == 0
                or (len(temp[1]) != 0 and temp[0][-1] < temp[1][-1])
                or (len(temp[2]) != 0 and temp[0][-1] < temp[2][-1])
                or (len(temp[3]) != 0 and temp[0][-1] < temp[3][-1])
            ):
                illegal[0] += 1
                skip = True
                break

            del temp[0][-1]
        elif c == "]":
            if (
                len(temp[1]) == 0
                or (len(temp[0]) != 0 and temp[1][-1] < temp[0][-1])
                or (len(temp[2]) != 0 and temp[1][-1] < temp[2][-1])
                or (len(temp[3]) != 0 and temp[1][-1] < temp[3][-1])
            ):
                illegal[1] += 1
                skip = True
                break

            del temp[1][-1]
        elif c == "}":
            if (
                len(temp[2]) == 0
                or (len(temp[0]) != 0 and temp[2][-1] < temp[0][-1])
                or (len(temp[1]) != 0 and temp[2][-1] < temp[1][-1])
                or (len(temp[3]) != 0 and temp[2][-1] < temp[3][-1])
            ):
                illegal[2] += 1
                skip = True
                break

            del temp[2][-1]
        elif c == ">":
            if (
                len(temp[3]) == 0
                or (len(temp[0]) != 0 and temp[3][-1] < temp[0][-1])
                or (len(temp[1]) != 0 and temp[3][-1] < temp[1][-1])
                or (len(temp[2]) != 0 and temp[3][-1] < temp[2][-1])
            ):
                illegal[3] += 1
                skip = True
                break

            del temp[3][-1]

    if not skip:
        incomplete.append(chunk)  # part 2

print(
    f"Part 1 - {illegal[0] * 3 + illegal[1] * 57 + illegal[2] * 1197 + illegal[3] * 25137}"
)

scores = []

for chunk in incomplete:
    temp = [[-1], [-1], [-1], [-1]]

    for i, c in enumerate(chunk):
        if c == "(":
            temp[0].append(i)
        elif c == "[":
            temp[1].append(i)
        elif c == "{":
            temp[2].append(i)
        elif c == "<":
            temp[3].append(i)
        elif c == ")":
            del temp[0][-1]
        elif c == "]":
            del temp[1][-1]
        elif c == "}":
            del temp[2][-1]
        elif c == ">":
            del temp[3][-1]

    score = 0

    while len(temp[0]) > 1 or len(temp[1]) > 1 or len(temp[2]) > 1 or len(temp[3]) > 1:
        score *= 5

        maxval = max([l[-1] for l in temp])
        if maxval == temp[0][-1]:
            score += 1
            del temp[0][-1]
        elif maxval == temp[1][-1]:
            score += 2
            del temp[1][-1]
        elif maxval == temp[2][-1]:
            score += 3
            del temp[2][-1]
        elif maxval == temp[3][-1]:
            score += 4
            del temp[3][-1]

    scores.append(score)

scores = sorted(scores)

print(f"Part 2 - {scores[int(len(scores) / 2)]}")
