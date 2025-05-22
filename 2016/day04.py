from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)


def validate(name: str, checksum: str) -> bool:
    dictionary = {}
    length = 0

    for c in name:
        if c == "-":
            continue
        if c not in dictionary:
            dictionary[c] = 1
        else:
            dictionary[c] += 1
        length = max(length, dictionary[c])

    temp = [""] * (length + 1)

    for key in dictionary:
        temp[dictionary[key]] += key

    cs = ""
    for i in temp[::-1]:
        if i:
            cs += "".join(sorted(list(i)))
        if len(cs) >= 5:
            break

    return checksum == cs[:5]


# --- part 1 ---

sum = 0

for line in data:
    name, temp = line.rsplit("-", 1)
    id, checksum = temp.split("[")

    id = int(id)
    checksum = checksum.strip("]")

    if validate(name, checksum):
        sum += id

print(sum)

# --- part 2 ---

from string import ascii_lowercase


def advance(c: str, n: int) -> str:
    if c in "- ":
        if n % 2 == 0:
            return c
        elif c == "-":
            return " "
        else:
            return "-"
    i = ascii_lowercase.index(c)
    return ascii_lowercase[(i + n) % len(ascii_lowercase)]


for line in data:
    name, temp = line.rsplit("-", 1)
    id, _ = temp.split("[")

    id = int(id)

    decrypt = ""

    for c in name:
        decrypt += advance(c, id)

    if "north" in decrypt and "pole" in decrypt:
        print(decrypt, id)
        break
