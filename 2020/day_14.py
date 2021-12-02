# --- Day 14: Docking Data ---

with open("input/day_14.in", "r") as file:
    data = [line.strip("\n") for line in file]

# --- part 1 ---

mask_length = 36


def masked_value(mask, value):

    temp = bin(value)[2:]
    temp = "0" * (mask_length - len(temp)) + temp
    temp = list(temp)

    for i in range(mask_length):
        if mask[i] != "X":
            temp[i] = mask[i]

    return int("".join(temp), 2)


mask = ""
mem = {}

for line in data:
    if line[:4] == "mask":
        mask = line[7:]
    else:
        i = line.find("]")

        address = int(line[4:i])
        value = int(line[i + 4 :])

        mem[address] = masked_value(mask, value)

sum = 0

for address in mem:
    sum += mem[address]

print(sum)

# --- part 2 ---


def masked_address(mask, address):

    temp = bin(address)[2:]
    temp = "0" * (mask_length - len(temp)) + temp

    result = [""]

    for i in range(mask_length):
        if mask[i] == "0":  # unchanged
            for j in range(len(result)):
                result[j] += temp[i]
        elif mask[i] == "1":  # overwritten by 1
            for j in range(len(result)):
                result[j] += "1"
        else:  # floating
            n = len(result)
            for j in range(n):
                result.append(result[j] + "1")
                result[j] += "0"

    return result


mask = ""
mem = {}

for line in data:
    if line[:4] == "mask":
        mask = line[7:]
    else:
        i = line.find("]")

        address = int(line[4:i])
        value = int(line[i + 4 :])

        for j in masked_address(mask, address):
            mem[int(j, 2)] = value

sum = 0

for address in mem:
    sum += mem[address]

print(sum)
