from pathlib import Path
from functools import cache

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")


MAP = dict()

for line in data:
    a, b = line.strip().split(":")
    b = b.strip().split()
    MAP[a] = b


@cache
def num_of_path(start: str, end: str) -> int:
    num = 0
    try:
        for next in MAP[start]:
            if next == end:
                num += 1
            else:
                num += num_of_path(next, end)
    except:
        pass
    return num


# --- part 1 ---

print(num_of_path("you", "out"))

# --- part 2 ---

print(
    num_of_path("svr", "fft") * num_of_path("fft", "dac") * num_of_path("dac", "out")
    + num_of_path("svr", "dac") * num_of_path("dac", "fft") * num_of_path("fft", "out")
)
