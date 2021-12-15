import heapq
import math

data = open("input/day15.in", "r").read().strip("\n").split("\n")
cavern = [list(map(int, list(line))) for line in data]
row = len(cavern)
col = len(cavern[0])

# Dijkstra's algorithm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

visited = [[False for _ in range(col)] for _ in range(row)]
distance = [[float("inf") for _ in range(col)] for _ in range(row)]
distance[0][0] = 0

hq = []
for i in range(row):
    for j in range(col):
        if i == 0 and j == 0:
            heapq.heappush(hq, (0, [i, j]))
        else:
            heapq.heappush(hq, (float("inf"), [i, j]))

while not visited[row - 1][col - 1]:
    d, curr = heapq.heappop(hq)

    if visited[curr[0]][curr[1]]:
        continue

    if curr[0] != 0 and not visited[curr[0] - 1][curr[1]]:
        if d + cavern[curr[0] - 1][curr[1]] < distance[curr[0] - 1][curr[1]]:
            distance[curr[0] - 1][curr[1]] = d + cavern[curr[0] - 1][curr[1]]
            heapq.heappush(
                hq, (d + cavern[curr[0] - 1][curr[1]], [curr[0] - 1, curr[1]])
            )

    if curr[0] < row - 1 and not visited[curr[0] + 1][curr[1]]:
        if d + cavern[curr[0] + 1][curr[1]] < distance[curr[0] + 1][curr[1]]:
            distance[curr[0] + 1][curr[1]] = d + cavern[curr[0] + 1][curr[1]]
            heapq.heappush(
                hq, (d + cavern[curr[0] + 1][curr[1]], [curr[0] + 1, curr[1]])
            )

    if curr[1] != 0 and not visited[curr[0]][curr[1] - 1]:
        if d + cavern[curr[0]][curr[1] - 1] < distance[curr[0]][curr[1] - 1]:
            distance[curr[0]][curr[1] - 1] = d + cavern[curr[0]][curr[1] - 1]
            heapq.heappush(
                hq, (d + cavern[curr[0]][curr[1] - 1], [curr[0], curr[1] - 1])
            )

    if curr[1] < col - 1 and not visited[curr[0]][curr[1] + 1]:
        if d + cavern[curr[0]][curr[1] + 1] < distance[curr[0]][curr[1] + 1]:
            distance[curr[0]][curr[1] + 1] = d + cavern[curr[0]][curr[1] + 1]
            heapq.heappush(
                hq, (d + cavern[curr[0]][curr[1] + 1], [curr[0], curr[1] + 1])
            )

    visited[curr[0]][curr[1]] = True

print(f"Part 1 - {distance[row-1][col-1]}")

mult = 5

visited = [[False for _ in range(mult * col)] for _ in range(mult * row)]
distance = [[float("inf") for _ in range(mult * col)] for _ in range(mult * row)]
distance[0][0] = 0

hq = []
for i in range(mult * row):
    for j in range(mult * col):
        if i == 0 and j == 0:
            heapq.heappush(hq, (0, [i, j]))
        else:
            heapq.heappush(hq, (float("inf"), [i, j]))

while not visited[mult * row - 1][mult * col - 1]:
    d, curr = heapq.heappop(hq)

    if visited[curr[0]][curr[1]]:
        continue

    if curr[0] != 0 and not visited[curr[0] - 1][curr[1]]:
        temp = (
            cavern[(curr[0] - 1) % row][curr[1] % col]
            + math.floor((curr[0] - 1) / row)
            + math.floor(curr[1] / col)
        )
        while temp > 9:
            temp -= 9

        if d + temp < distance[curr[0] - 1][curr[1]]:
            distance[curr[0] - 1][curr[1]] = d + temp
            heapq.heappush(hq, (d + temp, [curr[0] - 1, curr[1]]))

    if curr[0] < mult * row - 1 and not visited[curr[0] + 1][curr[1]]:
        temp = (
            cavern[(curr[0] + 1) % row][curr[1] % col]
            + math.floor((curr[0] + 1) / row)
            + math.floor(curr[1] / col)
        )
        while temp > 9:
            temp -= 9

        if d + temp < distance[curr[0] + 1][curr[1]]:
            distance[curr[0] + 1][curr[1]] = d + temp
            heapq.heappush(hq, (d + temp, [curr[0] + 1, curr[1]]))

    if curr[1] != 0 and not visited[curr[0]][curr[1] - 1]:
        temp = (
            cavern[curr[0] % row][(curr[1] - 1) % col]
            + math.floor(curr[0] / row)
            + math.floor((curr[1] - 1) / col)
        )
        while temp > 9:
            temp -= 9

        if d + temp < distance[curr[0]][curr[1] - 1]:
            distance[curr[0]][curr[1] - 1] = d + temp
            heapq.heappush(hq, (d + temp, [curr[0], curr[1] - 1]))

    if curr[1] < mult * col - 1 and not visited[curr[0]][curr[1] + 1]:
        temp = (
            cavern[curr[0] % row][(curr[1] + 1) % col]
            + math.floor(curr[0] / row)
            + math.floor((curr[1] + 1) / col)
        )
        while temp > 9:
            temp -= 9

        if d + temp < distance[curr[0]][curr[1] + 1]:
            distance[curr[0]][curr[1] + 1] = d + temp
            heapq.heappush(hq, (d + temp, [curr[0], curr[1] + 1]))

    visited[curr[0]][curr[1]] = True

print(f"Part 2 - {distance[mult * row-1][mult * col-1]}")
