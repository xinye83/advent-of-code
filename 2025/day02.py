from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n")


def is_valid_1(num: int) -> bool:
    num_str = str(num)

    if len(num_str) % 2 == 1:
        return True

    half = int(len(num_str) / 2)

    for i in range(half):
        if num_str[i] != num_str[i + half]:
            return True

    return False


def is_valid_2(num: int) -> bool:
    num_str = str(num)

    for l in range(1, len(num_str)):
        if len(num_str) % l != 0:
            continue
        r = int(len(num_str) / l)

        temp = False
        for i in range(1, r):
            if num_str[:l] != num_str[i * l : (i + 1) * l]:
                temp = True
                break

        if not temp:
            return False

    return True


ids1 = 0
ids2 = 0

for item in data.split(","):
    lo, hi = item.split("-")

    for i in range(int(lo), int(hi) + 1):
        if not is_valid_1(i):
            ids1 += i
        if not is_valid_2(i):
            ids2 += i

print(ids1)
print(ids2)
