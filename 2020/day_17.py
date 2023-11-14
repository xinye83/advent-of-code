# --- Day 17: Conway Cubes ---

data = open("input/day_17.in", "r").read().strip("\n").split("\n")

import itertools
import math


class ConwayCube:
    def __init__(self, dimension, grid):

        self.dimension = dimension

        # range of each dimensions
        self.range = [[math.inf, -math.inf] for i in range(dimension)]

        # coordinates of active cubes
        self.active = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    self.range[0][0] = min(i, self.range[0][0])
                    self.range[0][1] = max(i, self.range[0][1])

                    self.range[1][0] = min(j, self.range[1][0])
                    self.range[1][1] = max(j, self.range[1][1])

                    for k in range(2, dimension):
                        self.range[k][0] = 0
                        self.range[k][1] = 0

                    self.active.append([i, j] + [0 for k in range(2, dimension)])

    def __len__(self):
        return len(self.active)

    def __active_neighbors(self, coordinate):
        count = 0
        temp = [[-1, 0, 1] for i in range(self.dimension)]

        for i in itertools.product(*temp):
            ii = list(i)

            is_zero = True
            for j in ii:
                if j != 0:
                    is_zero = False
                    break

            if (
                    not is_zero
                    and [ii[j] + coordinate[j] for j in range(self.dimension)]
                    in self.active
            ):
                count += 1

        return count

    def cycle(self, num):
        if num <= 0:
            return
        elif num > 1:
            i = 0
            while i < num:
                self.cycle(1)
                i += 1
            return

        next = []

        # this part is probably really bad
        temp = [
            range(self.range[i][0] - 1, self.range[i][1] + 2)
            for i in range(self.dimension)
        ]

        for coordinate in itertools.product(*temp):
            coordinate2 = list(coordinate)

            count = self.__active_neighbors(coordinate2)

            if (coordinate2 in self.active and count in [2, 3]) or (
                    coordinate2 not in self.active and count == 3
            ):
                next.append(coordinate2)

        self.active = next

        # re-compute ranges
        self.range = [[math.inf, -math.inf] for i in range(self.dimension)]

        for coordinate in self.active:
            for i in range(self.dimension):
                self.range[i][0] = min(self.range[i][0], coordinate[i])
                self.range[i][1] = max(self.range[i][1], coordinate[i])


# --- part 1 ---

state1 = ConwayCube(3, data)
state1.cycle(6)

print(len(state1))

# --- part 2 ---

state2 = ConwayCube(4, data)
state2.cycle(6)

print(len(state2))
