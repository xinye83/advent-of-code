from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n\n")
)

patterns = data[0].split(", ")
designs = data[1].split("\n")

# --- part 1 ---


def is_valid(design: str, index: int) -> bool:
    if index == len(design):
        return True
    valid = False
    for pattern in patterns:
        if (
            index + len(pattern) <= len(design)
            and design[index : index + len(pattern)] == pattern
        ):
            valid = valid or is_valid(design, index + len(pattern))
    return valid


result = 0

for design in designs:
    if is_valid(design, 0):
        result += 1

print(result)

# --- part 2 ---


def count_valid(design: str, index: int, dp: list[int]) -> int:
    if dp[index] >= 0:
        return dp[index]

    dp[index] = 0
    for pattern in patterns:
        if (
            index + len(pattern) <= len(design)
            and design[index : index + len(pattern)] == pattern
        ):
            dp[index] += count_valid(design, index + len(pattern), dp)
    return dp[index]


result = 0

for design in designs:
    dp = [-1] * len(design) + [1]
    result += count_valid(design, 0, dp)

print(result)
