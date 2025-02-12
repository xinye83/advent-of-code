from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---


def process(number: int) -> int:
    number = ((number << 6) ^ number) % 16777216
    number = ((number >> 5) ^ number) % 16777216
    number = ((number << 11) ^ number) % 16777216
    return number


sum = 0

for number in data:
    number = int(number)
    for _ in range(2000):
        number = process(number)
    sum += number

print(sum)

# --- part 2 ---

# 0 <= diff + 9 < 19
# (d1, d2, d3, d4) -> d1 + d2 * 19 + d3 * 19^2 + d4 * 19^3


def seq_to_int(seq: list[int]) -> int:
    return (
        (seq[0] + 9)
        + (seq[1] + 9) * 19
        + (seq[2] + 9) * 19 * 19
        + (seq[3] + 9) * 19 * 19 * 19
    )


map = dict()

for number in data:
    this = int(number)
    seq = []

    temp = dict()
    for _ in range(2000):
        next = process(this)
        seq.append(next % 10 - this % 10)

        if len(seq) > 4:
            seq.pop(0)

        if len(seq) == 4:
            i = seq_to_int(seq)
            if i not in temp:
                temp[i] = next % 10

        this = next

    for key, value in temp.items():
        if key in map:
            map[key] += value
        else:
            map[key] = value

m = 0
for key in map:
    m = max(m, map[key])

print(m)
