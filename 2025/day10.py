from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

# --- part 1 ---


def to_diagram(string: str) -> list[int]:
    ret = list()

    for c in string:
        if c == ".":
            ret.append(0)
        elif c == "#":
            ret.append(1)
        else:
            raise Exception()

    return ret


def to_wires(string: str) -> list[list[int]]:
    ret = list()

    for wire in string.split():
        ret.append(list(map(int, wire[1:-1].split(","))))

    return ret


CACHE = {n: dict() for n in range(20)}


def n_sum_k(n: int, k: int) -> list[list[int]]:
    """
    Return all possible combinations where n non-negative integers sum to k
    """
    assert n >= 1
    assert k >= 0

    if k in CACHE[n]:
        return CACHE[n][k]

    if k == 0:
        CACHE[n][k] = [[0] * n]
        return CACHE[n][k]
    if n == 1:
        CACHE[n][k] = [[k]]
        return CACHE[n][k]

    ret = list()
    for i in range(k + 1):
        ret += [item + [i] for item in n_sum_k(n - 1, k - i)]

    CACHE[n][k] = ret
    return CACHE[n][k]


def validate(diagram, wires, combo) -> bool:
    result = [0] * len(diagram)

    for i in range(len(wires)):
        for j in range(len(wires[i])):
            result[wires[i][j]] += combo[i]

    for i in range(len(diagram)):
        if (diagram[i] - result[i]) % 2 == 1:
            return False

    return True


sum_of_press = 0

for line in data:
    i = line.index("]")
    j = line.index("{")

    diagram = to_diagram(line[1:i])
    wires = to_wires(line[i + 1 : j])

    press = 0
    correct = False

    while True:
        for combo in n_sum_k(len(wires), press):
            if validate(diagram, wires, combo):
                correct = True
                break

        if correct:
            break

        press += 1

    sum_of_press += press

print(sum_of_press)

# --- part 2 ---

# https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

from functools import cache
from itertools import combinations


def patterns(coeffs: list[tuple[int, ...]]) -> dict[tuple[int, ...], int]:
    out = {}
    num_buttons = len(coeffs)
    num_variables = len(coeffs[0])
    for pattern_len in range(num_buttons + 1):
        for buttons in combinations(range(num_buttons), pattern_len):
            pattern = tuple(
                map(sum, zip((0,) * num_variables, *(coeffs[i] for i in buttons)))
            )
            if pattern not in out:
                out[pattern] = pattern_len
    return out


def solve_single(coeffs: list[tuple[int, ...]], goal: tuple[int, ...]) -> int:
    pattern_costs = patterns(coeffs)

    @cache
    def solve_single_aux(goal: tuple[int, ...]) -> int:
        if all(i == 0 for i in goal):
            return 0
        answer = 1000000
        for pattern, pattern_cost in pattern_costs.items():
            if all(i <= j and i % 2 == j % 2 for i, j in zip(pattern, goal)):
                new_goal = tuple((j - i) // 2 for i, j in zip(pattern, goal))
                answer = min(answer, pattern_cost + 2 * solve_single_aux(new_goal))
        return answer

    return solve_single_aux(goal)


def solve(raw: str):
    answer = 0
    lines = raw.splitlines()
    for I, L in enumerate(lines, 1):
        _, *coeffs, goal = L.split()
        goal = tuple(int(i) for i in goal[1:-1].split(","))
        coeffs = [[int(i) for i in r[1:-1].split(",")] for r in coeffs]
        coeffs = [tuple(int(i in r) for i in range(len(goal))) for r in coeffs]

        subanswer = solve_single(coeffs, goal)
        print(f"Line {I}/{len(lines)}: answer {subanswer}")
        answer += subanswer
    print(answer)


solve(Path(__file__.replace(".py", ".in")).read_text())
