from pathlib import Path
import numpy as np

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".ex.in")).read_text().strip("\n")
)

# --- part 1 ---

indices = [int(i) for i in data]
indices = np.cumsum(indices).tolist()

in_file = True

cur_index = 0
cur_len = indices[0]

backup_index = len(indices) - 1
backup_len = indices[-1] - indices[-2]

id_num = 0

checksum = 0

while cur_index < backup_index:
    if in_file:
        checksum += id_num * cur_index
    else:
        checksum += id_num * backup_index
        backup_len -= 1

    cur_len -= 1
    id_num += 1

    if cur_len == 0:
        in_file = not in_file
        cur_index += 1
        cur_len = indices[cur_index + 1] - indices[cur_index]

    while backup_len == 0:
        backup_index -= 2
        backup_len = indices[backup_index + 1] - indices[backup_index]

print(checksum)
