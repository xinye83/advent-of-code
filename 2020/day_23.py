# --- Day 23: Crab Cups ---

input = 364289715


# --- part 1 ---


def move(labels, steps):
    if steps > 1:
        for i in range(steps):
            labels = move(labels, 1)
        return labels

    current = labels[0]
    pickup = labels[1:4]
    del labels[1:4]

    destination = current - 1
    while destination not in labels:
        destination -= 1
        if destination < min(labels):
            destination = max(labels)

    index = labels.index(destination)

    labels = labels[1: index + 1] + pickup + labels[index + 1:] + [current]

    return labels


labels = [int(c) for c in str(input)]
labels = move(labels, 100)

i = labels.index(1)

print("".join([str(n) for n in labels[i + 1:] + labels[:i]]))


# --- part 2 ---

# Thanks to this reddit comment by kraven001 at
# https://www.reddit.com/r/adventofcode/comments/kiq1vl/
#   2020_day_23_part_2_runtime_comparison/ggsfpcu?utm_source
#   =share&utm_medium=web2x&context=3
#
# "The faster solution is to use an array to store the cups
#   (indices are cup values, and values are "next cups").
# This way you are just doing in place value updates and have
#   instant search times."


class Cups:
    def __init__(self, label):
        self.len = len(label)

        self.label = [-1] * (self.len + 1)

        for i in range(len(label) - 1):
            self.label[label[i]] = label[i + 1]

        self.label[label[-1]] = label[0]

        self.cur = label[0]

        self.pickup = [-1, -1, -1]

    def move(self, step=1):

        if step != 1:
            for i in range(step):
                self.move()

        temp = self.cur

        for i in range(3):
            self.pickup[i] = self.label[temp]
            temp = self.label[temp]

        dest = self.cur

        while dest == self.cur or dest in self.pickup:
            dest -= 1
            if dest < 1:
                dest = self.len

        self.label[self.cur] = self.label[temp]
        self.label[temp] = self.label[dest]
        self.label[dest] = self.pickup[0]

        self.cur = self.label[self.cur]


cups = Cups(
    [int(c) for c in str(input)] + [c for c in range(len(str(input)) + 1, 1000001)]
)
cups.move(10000000)

print(cups.label[1])
print(cups.label[cups.label[1]])
print(cups.label[1] * cups.label[cups.label[1]])
