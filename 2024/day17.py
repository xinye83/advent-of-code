import copy
from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

# --- part 1 ---

a = int(data[0][len("Register A: ") :])
b = int(data[1][len("Register B: ") :])
c = int(data[2][len("Register C: ") :])
program = [int(i) for i in data[-1][len("Program: ") :].split(",")]

pointer = 0
output = []


def instruction(a, b, c, pointer, output):
    opcode = program[pointer]
    operand = program[pointer + 1]

    assert 0 <= opcode < 8
    assert 0 <= operand < 8

    jump = False
    literal = operand
    combo = literal

    match literal:
        case 4:
            combo = a
        case 5:
            combo = b
        case 6:
            combo = c
        case 7:
            raise Exception("invalid operand")

    match opcode:
        case 0:
            a >>= combo
        case 1:
            b ^= literal
        case 2:
            b = combo % 8
        case 3:
            if a != 0:
                jump = True
                pointer = literal
        case 4:
            b ^= c
        case 5:
            output.append(combo % 8)
        case 6:
            b = a >> combo
        case 7:
            c = a >> combo

    if not jump:
        pointer += 2

    return a, b, c, pointer, output


while pointer < len(program):
    a, b, c, pointer, output = instruction(a, b, c, pointer, output)

print(",".join([str(i) for i in output]))

# --- part 2 ---

# search from the most significant 8-bit digit in a

i = len(program) - 1
value = [""]

while i >= 0:
    new_value = []

    for v in value:
        for d in range(8):
            a = int(v + str(d), 8)
            b = int(data[1][len("Register B: ") :])
            c = int(data[2][len("Register C: ") :])
            pointer = 0
            output = []

            while pointer < len(program):
                a, b, c, pointer, output = instruction(a, b, c, pointer, output)

            if output == program[i:]:
                new_value.append(v + str(d))

    i -= 1
    value = new_value

print(min([int(i, 8) for i in value]))
