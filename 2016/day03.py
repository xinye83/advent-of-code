from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)


def valid(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a


# --- part 1 ---

possible = 0

for triangle in data:
    a, b, c = triangle.split()
    possible += valid(int(a), int(b), int(c))

print(possible)

# --- part 2 ---

possible = 0
t1 = []
t2 = []
t3 = []


for row in data:
    a, b, c = row.split()

    t1.append(int(a))
    t2.append(int(b))
    t3.append(int(c))

    if len(t1) == 3:
        possible += valid(*t1)
        possible += valid(*t2)
        possible += valid(*t3)

        t1 = []
        t2 = []
        t3 = []

print(possible)
