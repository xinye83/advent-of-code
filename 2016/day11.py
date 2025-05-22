from enum import IntEnum, auto


class Material(IntEnum):
    polonium = auto()
    thulium = auto()
    promethium = auto()
    ruthenium = auto()
    cobalt = auto()


class Device(IntEnum):
    chip = auto()
    generator = auto()


class Item:
    def __init__(self, material: Material, device: Device):
        if not material or not device:
            raise Exception
        self._material = material
        self._device = device

    def __str__(self):
        return str(self._material) + str(self._device)

    def __lt__(self, other):
        return (
            self._material < other._material
            or self._material == other._material
            and self._device < other._device
        )


initial = [
    None,
    [
        Item(Material.polonium, Device.generator),
        Item(Material.thulium, Device.generator),
        Item(Material.thulium, Device.chip),
        Item(Material.promethium, Device.generator),
        Item(Material.ruthenium, Device.generator),
        Item(Material.ruthenium, Device.chip),
        Item(Material.cobalt, Device.generator),
        Item(Material.cobalt, Device.chip),
    ],
    [
        Item(Material.polonium, Device.chip),
        Item(Material.promethium, Device.chip),
    ],
    [],
    [],
]


def floor_to_str(step, elevator, floors) -> str:
    return (
        "S"
        + str(step)
        + "E"
        + str(elevator)
        + "F1"
        + "".join([str(item) for item in sorted(floors[1])])
        + "F2"
        + "".join([str(item) for item in sorted(floors[2])])
        + "F3"
        + "".join([str(item) for item in sorted(floors[3])])
        + "F4"
        + "".join([str(item) for item in sorted(floors[4])])
    )


def str_to_floor(string: str) -> tuple[int, int, list]:
    i = 1
    while string[i].isnumeric():
        i += 1
    step = int(string[1:i])

    i += 1
    elevator = int(string[i])

    i += 1
    floors = [None, [], [], [], []]
    c = 0
    while i < len(string):
        if string[i] == "F":
            c = int(string[i + 1])
        else:
            floors[c].append(Item(Material(int(string[i])), Device(int(string[i + 1]))))
        i += 2

    return step, elevator, floors


# --- part 1 ---

# breath-first search

i = 0
step = 0
elevator = 1
stack = [floor_to_str(step, elevator, initial)]

cache = set()
cache.add(stack[i])

while i < len(stack):
    s = stack[i]
    step, elevator, floors = str_to_floor(s)

    if not (floors[1] and floors[2] and floors[3]):
        break

    i += 1

print(step)
