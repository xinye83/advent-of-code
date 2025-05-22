from pathlib import Path
import copy

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split()
)

# --- part 1 ---


def blink(stones: list[str]) -> list[str]:
    i = 0
    while i < len(stones):
        if stones[i] == "0":
            stones[i] = "1"
        elif not len(stones[i]) % 2:
            a = stones[i][0 : int(len(stones[i]) / 2)]
            b = stones[i][int(len(stones[i]) / 2) :].lstrip("0")
            if not b:
                b = "0"
            stones[i] = a
            stones.insert(i + 1, b)
            i += 1
        else:
            stones[i] = str(int(stones[i]) * 2024)

        i += 1


stones = copy.deepcopy(data)

for i in range(25):
    blink(stones)

print(len(stones))


# --- part 2 ---


def update(map, key, value):
    if key not in map:
        map[key] = value
    else:
        map[key] += value


def blink2(stones: dict[int, int]) -> dict[int, int]:
    ret = dict()

    for key, value in stones.items():
        if key == 0:
            update(ret, 1, value)
        elif len(str(key)) % 2 == 0:
            s = str(key)
            a = int(s[0 : int(len(s) / 2)])
            b = int(s[int(len(s) / 2) :])
            update(ret, a, value)
            update(ret, b, value)
        else:
            update(ret, key * 2024, value)

    return ret


stones2 = dict()

for i in data:
    update(stones2, int(i), 1)

for _ in range(75):
    stones2 = blink2(stones2)

l = 0
for key in stones2:
    l += stones2[key]

print(l)
