from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---

len = len(data[0])
msg = ["*"] * len

freq: list[dict[str, int]] = [{"*": 0} for _ in range(len)]

for line in data:
    for i in range(len):
        c = line[i]

        if c not in freq[i]:
            freq[i][c] = 1
        else:
            freq[i][c] += 1

        if freq[i][c] > freq[i][msg[i]]:
            msg[i] = c

print("".join(msg))

# --- part 2 ---

msg2 = ["a"] * len

for i in range(len):
    for char, num in freq[i].items():
        if char == "*":
            continue
        if num < freq[i][msg2[i]]:
            msg2[i] = char

print("".join(msg2))
