from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

row = len(data)
col = len(data[0])


# --- part 1 ---


pattern = "XMAS"
count = 0


for i in range(row):
    for j in range(col):
        for ii in (-1, 0, 1):
            for jj in (-1, 0, 1):
                if ii == 0 and jj == 0:
                    continue

                valid = True

                for kk in range(len(pattern)):
                    if (
                        i + ii * kk < 0
                        or i + ii * kk >= row
                        or j + jj * kk < 0
                        or j + jj * kk >= col
                        or data[i + ii * kk][j + jj * kk] != pattern[kk]
                    ):
                        valid = False
                        break

                if valid:
                    count += 1


print(count)


# --- part 2 ---

count = 0

for i in range(row):
    for j in range(col):
        if i == 0 or i == row - 1 or j == 0 or j == col - 1 or data[i][j] != "A":
            continue

        m = 0
        s = 0

        for ii in (i - 1, i + 1):
            for jj in (j - 1, j + 1):
                if data[ii][jj] == "M":
                    m += 1
                elif data[ii][jj] == "S":
                    s += 1

        if m != 2 or s != 2 or data[i - 1][j - 1] == data[i + 1][j + 1]:
            continue

        count += 1
print(count)
