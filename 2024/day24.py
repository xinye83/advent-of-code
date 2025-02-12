import copy
from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n\n")
)


VALUES = dict()

for gate in data[0].split("\n"):
    a, b = gate.split(": ")
    VALUES[a] = int(b)

WIRES = dict()

for wire in data[1].split("\n"):
    a, b = wire.split(" -> ")
    WIRES[b] = tuple(a.split(" "))

# --- part 1 ---

values = copy.deepcopy(VALUES)
wires = copy.deepcopy(WIRES)


def get_wire_value(wire: str) -> int:
    if wire in values:
        return values[wire]

    if wire not in wires:
        raise Exception

    a = get_wire_value(wires[wire][0])
    b = get_wire_value(wires[wire][2])

    if wires[wire][1] == "AND":
        c = a & b
    elif wires[wire][1] == "OR":
        c = a | b
    elif wires[wire][1] == "XOR":
        c = a ^ b
    else:
        raise Exception

    values[wire] = c
    return c


def get_value(string: str) -> int:
    assert string in "xyz"

    temp = ""
    index = 0

    while True:
        wire = str(index)
        if len(wire) == 1:
            wire = "0" + wire
        wire = string + wire

        if wire not in wires and wire not in values:
            break

        temp = str(get_wire_value(wire)) + temp
        index += 1

    return int(temp, 2)


print(get_value("z"))

# --- part 2 ---

pool = []
for wire in WIRES:
    a, b, c = WIRES[wire]

    if wire == "z45":
        continue

    # If the output of a gate is z, then the operation has to be XOR unless it is the last bit.
    if wire[0] == "z" and b != "XOR":
        pool.append(wire)
        continue

    # If the output of a gate is not z and the inputs are not x, y then it has to be AND / OR, but not XOR.
    if wire[0] != "z" and a[0] not in "xy" and c[0] not in "xy" and b == "XOR":
        pool.append(wire)
        continue

    # If you have a XOR gate with inputs x, y, there must be another XOR gate with this gate as an input. Search through all gates for an XOR-gate with this gate as an input; if it does not exist, your (original) XOR gate is faulty.
    # Similarly, if you have an AND-gate, there must be an OR-gate with this gate as an input. If that gate doesn't exist, the original AND gate is faulty.
    # (These don't apply for the gates with input x00, y00).
    if a[1:] == "00" or c[1:] == "00":
        continue

    if a[0] in "xy" and c[0] in "xy" and b == "XOR":
        valid = False
        for wire2 in WIRES:
            if WIRES[wire2][1] == "XOR" and (
                WIRES[wire2][0] == wire or WIRES[wire2][2] == wire
            ):
                valid = True
                break
        if not valid:
            pool.append(wire)
    elif a[0] in "xy" and c[0] in "xy" and b == "AND":
        valid = False
        for wire2 in WIRES:
            if WIRES[wire2][1] == "OR" and (
                WIRES[wire2][0] == wire or WIRES[wire2][2] == wire
            ):
                valid = True
                break
        if not valid:
            pool.append(wire)

pool.sort()
print(",".join(pool))
