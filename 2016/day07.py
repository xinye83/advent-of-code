from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---


def is_abba(string: str, position: int) -> bool:
    if position < 0 or position + 4 > len(string):
        return False

    if (
        string[position] in "[]"
        or string[position + 1] in "[]"
        or string[position + 2] in "[]"
        or string[position + 3] in "[]"
    ):
        return False

    if string[position] == string[position + 1]:
        return False

    if string[position + 1] != string[position + 2]:
        return False

    if string[position] != string[position + 3]:
        return False

    return True


valid_tls = 0

for line in data:
    in_bracket = False
    abba_in_bracket = 0
    abba_out_bracket = 0

    for i in range(len(line)):
        if line[i] == "[":
            in_bracket = True
        elif line[i] == "]":
            in_bracket = False

        if is_abba(line, i):
            if in_bracket:
                abba_in_bracket += 1
            else:
                abba_out_bracket += 1

    if abba_in_bracket == 0 and abba_out_bracket > 0:
        valid_tls += 1


print(valid_tls)

# --- part 2 ---


def is_aba(string: str, position: int) -> bool:
    if position < 0 or position + 3 > len(string):
        return False

    if (
        string[position] in "[]"
        or string[position + 1] in "[]"
        or string[position + 2] in "[]"
    ):
        return False

    if string[position] == string[position + 1]:
        return False

    if string[position] != string[position + 2]:
        return False

    return True


valid_ssl = 0

for line in data:
    in_bracket = False
    m = dict()

    is_valid = False

    for i in range(len(line)):
        if line[i] == "[":
            in_bracket = True
        elif line[i] == "]":
            in_bracket = False

        if not is_aba(line, i):
            continue

        if in_bracket:
            key = line[i : i + 2]
            if key not in m:
                m[key] = 1
            elif m[key] == -1:
                is_valid = True
                break
        else:
            key = line[i + 1 : i + 3]
            if key not in m:
                m[key] = -1
            elif m[key] == 1:
                is_valid = True
                break

    valid_ssl += is_valid

print(valid_ssl)
