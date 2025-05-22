import functools
from pathlib import Path

data = (Path(__file__).parent / 'input' / 'day13.in').read_text().strip('\n').split('\n\n')


def process_packet(line: str, start: int, end: int):
    ret = []

    i = 1
    while start + i < end:
        if line[start + i] == ']':
            break
        elif line[start + i] == '[':
            c = 1
            j = i
            while c > 0:
                j += 1
                if line[start + j] == '[':
                    c += 1
                elif line[start + j] == ']':
                    c -= 1

            ret.append(process_packet(line, start + i, start + j))
            j += 1
        else:
            j = i
            while start + j < end and line[start + j] not in ',]':
                j += 1
            ret.append(int(line[start + i: start + j]))

        i = j + 1

    return ret


# 1: right order
# -1: wrong order
# 0: same order
def compare_packet(left: list, right: list):
    ok = True
    i = 0
    while i < len(left):
        if i == len(right):
            return -1

        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
        else:
            l1 = [left[i]] if isinstance(left[i], int) else left[i]
            l2 = [right[i]] if isinstance(right[i], int) else right[i]

            r = compare_packet(l1, l2)
            if r != 0:
                return r

        i += 1

    if i == len(right):
        return 0

    return 1


sum_index = 0
index = 1

for packet in data:
    temp1, temp2 = packet.split('\n')

    left = process_packet(temp1, 0, len(temp1))
    right = process_packet(temp2, 0, len(temp2))

    if compare_packet(left, right) == 1:
        sum_index += index

    index += 1

print(sum_index)

# part 2

packets = (Path(__file__).parent / 'input' / 'day13.in').read_text().strip('\n').replace('\n\n', '\n').split('\n')
packets = [process_packet(line, 0, len(line)) for line in packets]
packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=functools.cmp_to_key(compare_packet), reverse=True)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
