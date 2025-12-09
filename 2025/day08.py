from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

# --- part 1 ---

boxes = [list(map(int, line.split(","))) for line in data]
distances = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distances.append(
            (
                (boxes[i][0] - boxes[j][0]) ** 2
                + (boxes[i][1] - boxes[j][1]) ** 2
                + (boxes[i][2] - boxes[j][2]) ** 2,
                i,
                j,
            )
        )

distances.sort(key=lambda x: x[0])

circuits = []
visited = [False] * len(boxes)

for i in range(len(boxes)):
    if visited[i]:
        continue

    circuit = []
    stack = [i]
    while stack:
        j = stack.pop()
        if visited[j] or j in circuit:
            continue

        visited[j] = True
        circuit.append(j)

        for d in distances[:1000]:
            if d[1] == j:
                stack.append(d[2])
            elif d[2] == j:
                stack.append(d[1])

    circuits.append(circuit)

circuits.sort(key=lambda x: len(x))

print(len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3]))

# --- part 2 ---


def find_box_in_circuits(box: int) -> int:
    for i in range(len(circuits)):
        if box in circuits[i]:
            return i
    raise Exception()


for i in range(1000, len(distances)):
    if len(circuits) == 1:
        break

    i1 = find_box_in_circuits(distances[i][1])
    i2 = find_box_in_circuits(distances[i][2])

    if i1 == i2:
        continue

    circuits[i1] += circuits[i2]
    circuits.pop(i2)

print(boxes[distances[i - 1][1]][0] * boxes[distances[i - 1][2]][0])
