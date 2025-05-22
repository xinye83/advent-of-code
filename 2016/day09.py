from pathlib import Path

data: str = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .replace(" ", "")
)


def get_marker(position: int) -> tuple[int, int, int]:
    assert data[position] == "("

    j = 1
    while data[position + j] != ")":
        j += 1

    l, r = data[position + 1 : position + j].split("x")
    l = int(l)
    r = int(r)

    # additional position of ), length of repeat, number of repeat
    return j, l, r


# --- part 1 ---

pos = 0
length = 0

while pos < len(data):
    if data[pos].isalpha():
        length += 1
        pos += 1
        continue

    # data[pos] == "("
    j, l, r = get_marker(pos)
    length += l * r
    pos += j + l + 1

print(length)

# --- part 2 ---


def decompressed_length(start: int, end: int) -> int:
    length = 0
    pos = start

    while pos < end:
        if data[pos].isalpha():
            length += 1
            pos += 1
            continue

        # data[pos] == "("
        j, l, r = get_marker(pos)
        length += decompressed_length(pos + j + 1, pos + j + l + 1) * r
        pos += j + l + 1

    return length


print(decompressed_length(0, len(data)))
