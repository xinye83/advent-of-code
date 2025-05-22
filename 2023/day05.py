import re
from util import *

data = get_input().split("\n\n")

# --- part 1 ---


def convert(lst, map):
    ret = []
    for x in lst:
        y = None
        for line in map.split("\n")[1:]:
            dst, src, wid = line.split()
            if x in range(int(src), int(src) + int(wid)):
                y = x - int(src) + int(dst)
                break
        if not y:
            y = x
        ret.append(y)

    return ret


seed = [int(i) for i in data[0].split(":")[-1].split()]

for map in data[1:]:
    seed = convert(seed, map)

print(min(seed))

# --- part 2 ---


def convert_2(lst, map):
    ret = []
    for x in lst:
        for line in map.split("\n")[1:]:
            dst, src, wid = line.split()
            dst = int(dst)
            src = int(src)
            wid = int(wid)


seed = re.findall("\d+ \d+", data[0].split(":")[-1])
seed = [[int(i.split()[0]), int(i.split()[1])] for i in seed]
seed.sort()

for map in data[1:]:
    seed = convert_2(seed, map)
