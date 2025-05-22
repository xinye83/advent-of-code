from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)


_NUMERIC = {"key": "789456123 0A", "row": 4, "col": 3}
_DIRECTION = {"key": " ^A<v>", "row": 2, "col": 3}


def sequence_p2p(start: str, end: str) -> tuple[str]:
    """
    return the best sequence(s) on a directional keypad for moving from start to end
    on a numeric or directional keypad

    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+

        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """
    if len(start) != 1 or len(end) != 1 or start == " " or end == " ":
        raise ValueError

    if start in _NUMERIC["key"] and end in _NUMERIC["key"]:
        key = _NUMERIC["key"]
        col = _NUMERIC["col"]
    elif start in _DIRECTION["key"] and end in _DIRECTION["key"]:
        key = _DIRECTION["key"]
        col = _DIRECTION["col"]
    else:
        raise ValueError

    # index = y + col * x
    y1 = key.index(start) % col
    x1 = int((key.index(start) - y1) / col)
    y2 = key.index(end) % col
    x2 = int((key.index(end) - y2) / col)

    dx = "v" if x1 <= x2 else "^"
    dy = ">" if y1 <= y2 else "<"

    ret = []
    if key[x2 * col + y1] != " ":
        ret.append(dx * abs(x1 - x2) + dy * abs(y1 - y2) + "A")
    if key[x1 * col + y2] != " ":
        ret.append(dy * abs(y1 - y2) + dx * abs(x1 - x2) + "A")

    return tuple(set(ret))


_SEQ = dict()
_CACHE = dict()


def update_seq(start: str, end: str) -> None:
    if start not in _SEQ:
        _SEQ[start] = dict()
    if end not in _SEQ[start]:
        _SEQ[start][end] = sequence_p2p(start, end)


def sequence_p2p_cached(start: str, end: str, depth: int) -> int:
    assert depth > 0

    try:
        return _CACHE[start][end][depth]
    except:
        pass

    if start not in _CACHE:
        _CACHE[start] = dict()
    if end not in _CACHE[start]:
        _CACHE[start][end] = dict()

    update_seq(start, end)

    if depth == 1:
        _CACHE[start][end][depth] = len(_SEQ[start][end][0])
    else:
        seq = _SEQ[start][end]
        _CACHE[start][end][depth] = -1

        for s in seq:
            l = sequence_str_cached(s, depth - 1)
            if _CACHE[start][end][depth] == -1 or _CACHE[start][end][depth] > l:
                _CACHE[start][end][depth] = l

    return _CACHE[start][end][depth]


def sequence_str_cached(string: str, depth: int) -> int:
    assert depth > 0
    assert string[-1] == "A"

    ret = 0
    this = "A"
    for next in string:
        ret += sequence_p2p_cached(this, next, depth)
        this = next

    return ret


# --- part 1 ---

complexity = 0
depth = 3

for code in data:
    length = sequence_str_cached(code, depth)
    complexity += int(code.strip("A")) * length

print(complexity)

# --- part 2 ---

complexity2 = 0
depth = 26

for code in data:
    length = sequence_str_cached(code, depth)
    complexity2 += int(code.strip("A")) * length

print(complexity2)
