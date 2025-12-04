from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n")


def count(bank) -> list[list[int]]:
    ret = [None] + [[] for _ in range(9)]
    for i in range(len(bank)):
        ret[int(bank[i])].append(i)

    return ret


# --- part 1 ---


output = 0

for bank in data.split("\n"):
    c = count(bank)

    a = -1
    b = -1

    i = 9
    while i > 0:
        if c[i] and c[i][0] < len(bank) - 1:
            a = c[i][0]
            break
        i -= 1

    i = 9
    while i > 0:
        if c[i] and c[i][-1] > a:
            b = c[i][-1]
            break
        i -= 1

    output += int(bank[a] + bank[b])

print(output)

# --- part 2 ---


def get_max_num(index, length, bank, cache) -> int | None:
    """
    Return the maximum number of a fixed length from the bank (a string) on or after a position (index).
    cache[i][l] is the largest number of length l on or after position i in the bank.
    """

    if index + length > len(bank):
        return None

    if cache[index][length]:
        return cache[index][length]

    cache[index][length] = -1

    if length == 1:
        for c in bank[index:]:
            if cache[index][length] < int(c):
                cache[index][length] = int(c)
    else:
        for i in range(index, len(bank)):
            temp = get_max_num(i + 1, length - 1, bank, cache)
            if temp is None:
                continue

            temp = int(bank[i] + str(temp))
            if cache[index][length] < temp:
                cache[index][length] = temp

    return cache[index][length]


output2 = 0

for bank in data.split("\n"):
    output2 += get_max_num(
        0, 12, bank, [[None for _ in range(13)] for _ in range(len(bank))]
    )

print(output2)
