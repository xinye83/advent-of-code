from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n\n")
)

# --- part 1 ---

tokens = 0

for machine in data:
    machine = machine.split("\n")

    x1, y1 = machine[0][len("Button A: ") :].split(", ")
    x1 = int(x1[2:])
    y1 = int(y1[2:])

    x2, y2 = machine[1][len("Button B: ") :].split(", ")
    x2 = int(x2[2:])
    y2 = int(y2[2:])

    x, y = machine[2][len("Prize: ") :].split(", ")
    x = int(x[2:])
    y = int(y[2:])

    # min 3a + b
    # s.t.
    # 0 <= a <= 100, 0 <= b <= 100
    # | x1 x2 | | a | = | x |
    # | y1 y2 | | b |   | y |

    if x1 * y2 - x2 * y1 != 0:
        # | a | = 1/(x1*y2-x2*y1) | y2 -x2 | | x |
        # | b |                   | -y1 x1 | | y |
        # a = (y2 * x - x2 * y) / (x1 * y2 - x2 * y1)
        # b = (-y2 * x + x1 * y) / (x1 * y2 - x2 * y1)

        if not (y2 * x - x2 * y) % (x1 * y2 - x2 * y1) and not (-y1 * x + x1 * y) % (
            x1 * y2 - x2 * y1
        ):
            a = int((y2 * x - x2 * y) / (x1 * y2 - x2 * y1))
            b = int((-y1 * x + x1 * y) / (x1 * y2 - x2 * y1))
            tokens += 3 * int(a) + int(b)
        else:
            continue
    else:
        low = 401
        for a in range(101):
            for b in range(101):
                if x1 * a + x2 * b == x and y1 * a + y2 * b == y:
                    low = min(low, 3 * a + b)

        if low < 401:
            tokens += low

print(tokens)

# --- part 2 ---

ERROR = 10000000000000


def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(a - b, b)


def solve(x1, x2, x):
    """
    solve integer function x1 * a + x2 * b = x so that 3 * a + b is minimized
    return -1, -1 if no solution
    """
    m = gcd(x1, x2)
    if x % m:
        return -1, -1

    x1 = int(x1 / m)
    x2 = int(x2 / m)
    x = int(x / m)

    # the wanted solution (a, b) must satisfy 0 <= a < x2
    for a in range(x2):
        if x >= x1 * a and not (x - x1 * a) % x2:
            b = int((x - x1 * a) / x2)
            return a, b


tokens2 = 0

for machine in data:
    machine = machine.split("\n")

    x1, y1 = machine[0][len("Button A: ") :].split(", ")
    x1 = int(x1[2:])
    y1 = int(y1[2:])

    x2, y2 = machine[1][len("Button B: ") :].split(", ")
    x2 = int(x2[2:])
    y2 = int(y2[2:])

    x, y = machine[2][len("Prize: ") :].split(", ")
    x = int(x[2:]) + ERROR
    y = int(y[2:]) + ERROR

    # min 3a + b
    # s.t.
    # | x1 x2 | | a | = | x |
    # | y1 y2 | | b |   | y |

    if x1 * y2 - x2 * y1 != 0:
        # | a | = 1/(x1*y2-x2*y1) | y2 -x2 | | x |
        # | b |                   | -y1 x1 | | y |
        # a = (y2 * x - x2 * y) / (x1 * y2 - x2 * y1)
        # b = (-y2 * x + x1 * y) / (x1 * y2 - x2 * y1)

        if not (y2 * x - x2 * y) % (x1 * y2 - x2 * y1) and not (-y1 * x + x1 * y) % (
            x1 * y2 - x2 * y1
        ):
            a = int((y2 * x - x2 * y) / (x1 * y2 - x2 * y1))
            b = int((-y1 * x + x1 * y) / (x1 * y2 - x2 * y1))
            tokens2 += 3 * int(a) + int(b)
        else:
            continue
    else:
        # solve x1 a + x2 b = x
        a, b = solve(x1, x2, x)
        if a >= 0 and b >= 0:
            tokens2 += 3 * a + b

print(tokens2)
