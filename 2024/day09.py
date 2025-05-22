from pathlib import Path
import numpy as np

data = (Path(__file__).parent / (Path(__file__).stem + ".in")).read_text().strip("\n")

# indices[i] is the starting index of block i+1
# block 0 is file, block 1 is free space, ......
indices = [int(i) for i in data]
indices = np.cumsum(indices).tolist()

# --- part 1 ---

# block number, start index, end index
current = [0, 0, indices[0]]
current_id = 0
is_file = True

backup = [len(indices) - 1, indices[-2], indices[-1]]
backup_id = indices[-1] - 1

checksum = 0

while current_id <= backup_id:
    if not current[0] % 2:
        checksum += current_id * int(current[0] / 2)
    else:
        checksum += current_id * int(backup[0] / 2)
        backup_id -= 1

    current_id += 1

    if current_id == current[2]:
        current[0] += 1
        # skip block with 0 length
        while indices[current[0] - 1] == indices[current[0]]:
            current[0] += 1
        current[1] = indices[current[0] - 1]
        current[2] = indices[current[0]]

    if backup_id == backup[1] - 1:
        backup[0] -= 2
        # skip file block with 0 length
        while indices[backup[0] - 1] == indices[backup[0]]:
            backup[0] -= 2
        backup[1] = indices[backup[0] - 1]
        backup[2] = indices[backup[0]]
        backup_id = backup[2] - 1

# Part 1 example
# result: 1928
# sequence: 0099811188827773336446555566

print(checksum)

# --- part 2 ---

# blocks[i] is the i-th block represented by the starting index, file ID number (-1 for free space) and block length
blocks = [[0, 0, indices[0]]]

i = 1
while i < len(indices):
    start = indices[i - 1]
    length = indices[i] - indices[i - 1]

    if not i % 2:
        id = int(i / 2)
    else:
        id = -1

    if length > 0:
        blocks.append([start, id, length])

    i += 1

# remove free space at the end
while blocks[-1][1] == -1:
    blocks.pop()

for file_id in range(blocks[-1][1], 0, -1):
    i = 0
    while blocks[i][1] != file_id:
        i += 1

    for j in range(i):
        if blocks[j][1] != -1:
            continue
        if blocks[j][2] < blocks[i][2]:
            continue

        # new file block
        file = [blocks[j][0], file_id, blocks[i][2]]

        # mark old file block as free and merge with adjacent free blocks
        blocks[i][1] = -1

        if i > 0 and blocks[i - 1][1] == -1:
            blocks[i - 1][2] += blocks[i][2]
            blocks.pop(i)
            i -= 1

        if i + 1 < len(blocks) and blocks[i + 1][1] == -1:
            blocks[i][2] += blocks[i + 1][2]
            blocks.pop(i + 1)

        blocks[j][0] += file[2]
        blocks[j][2] -= file[2]
        if blocks[j][2] == 0:
            blocks.pop(j)

        blocks.insert(j, file)
        break

checksum_2 = 0
for block in blocks:
    if block[1] == -1:
        continue

    checksum_2 += block[1] * int((2 * block[0] + block[2] - 1) * block[2] / 2)

print(checksum_2)
