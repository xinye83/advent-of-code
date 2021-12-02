# --- Day 9: Encoding Error ---

data = []

with open("input/day_09.in", "r") as file:
    data = [int(line) for line in file]

# --- part 1 ---

preamble = 25
current = preamble

while True:
    # check if the current number is the sum of two
    # distinct numbers in previous 25 numbers

    valid = False
    temp = []

    for i in range(1, preamble + 1):

        if data[current - i] in temp:
            valid = True
            break

        temp.append(data[current] - data[current - i])

    if valid:
        current += 1
    else:
        target = data[current]
        print(data[current])
        break

# --- part 2 ---

start = 0
end = 1

while True:
    if end - start == 1:
        end += 1
        continue

    if sum(data[start:end]) == target:
        break
    elif sum(data[start:end]) > target:
        start += 1
    else:
        end += 1

print(max(data[start:end]) + min(data[start:end]))
