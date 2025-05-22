from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

wide = 101
tall = 103

# --- part 1 ---

second = 100

quadrant = [0, 0, 0, 0]

for robot in data:
    p, v = robot.split()
    p1, p2 = p[2:].split(",")
    v1, v2 = v[2:].split(",")

    p1 = (int(p1) + second * int(v1)) % wide
    p2 = (int(p2) + second * int(v2)) % tall

    if p1 == int(wide / 2) or p2 == int(tall / 2):
        continue

    quadrant[int(p1 < int(wide / 2)) + 2 * int(p2 < int(tall / 2))] += 1

print(quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3])

# --- part 2 ---


def advance(robots):
    for robot in robots:
        robot[0] += robot[2]
        robot[0] %= wide
        robot[1] += robot[3]
        robot[1] %= tall


robots = []

for robot in data:
    p, v = robot.split()
    p1, p2 = p[2:].split(",")
    v1, v2 = v[2:].split(",")

    robots.append([int(p1), int(p2), int(v1), int(v2)])

step = 0
while True:
    map = [[" " for _ in range(wide)] for _ in range(tall)]
    skip = False
    for robot in robots:
        if map[robot[1]][robot[0]] == "*":
            skip = True
            break
        map[robot[1]][robot[0]] = "*"
    if not skip:
        for line in map:
            print("".join(line))
        break

    advance(robots)
    step += 1

print(step)
