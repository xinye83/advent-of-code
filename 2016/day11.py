from enum import IntEnum, auto
import copy


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

# string: F1xxF2xxF3xxF4xxE1S12345


def floor_to_str(floors: list, elevator: int, step: int) -> str:
    return (
        "F1"
        + "".join([str(item) for item in sorted(floors[1])])
        + "F2"
        + "".join([str(item) for item in sorted(floors[2])])
        + "F3"
        + "".join([str(item) for item in sorted(floors[3])])
        + "F4"
        + "".join([str(item) for item in sorted(floors[4])])
        + "E"
        + str(elevator)
        + "S"
        + str(step)
    )


def str_to_floor(string: str) -> tuple[list, int, int]:
    floors = [None, [], [], [], []]
    i = 0
    c = 0
    while string[i] != "E":
        if string[i] == "F":
            c = int(string[i + 1])
        else:
            floors[c].append(Item(Material(int(string[i])), Device(int(string[i + 1]))))
        i += 2

    elevator = int(string[i + 1])
    step = int(string[i + 3 :])

    return floors, elevator, step


# --- part 1 ---

_LEN = 30


def is_valid_floor(floors: list) -> bool:
    for l in range(1, 5):
        chip = []
        generator = []

        for item in floors[l]:
            if item._device == Device.chip:
                chip.append(item._material)
            elif item._device == Device.generator:
                generator.append(item._material)

        pair = []
        for i in chip:
            if i in generator:
                chip.remove(i)
                generator.remove(i)
                pair.append(i)

        if chip and pair:
            return False

    return True


# breath-first search

stack = [floor_to_str(initial, 1, 0)]
idx = 0
cache = set()
cache.add(stack[idx][:_LEN])

while idx < len(stack):
    floors, elevator, step = str_to_floor(stack[idx])

    if not (floors[1] or floors[2] or floors[3]):
        break

    for l in (elevator - 1, elevator + 1):
        if l < 1 or l > 4:
            continue

        for i in range(len(floors[elevator])):
            for j in range(i, len(floors[elevator])):
                new_floors = copy.deepcopy(floors)

                new_floors[l].append(new_floors[elevator][j])
                del new_floors[elevator][j]

                if i != j:
                    new_floors[l].append(new_floors[elevator][i])
                    del new_floors[elevator][i]

                if not is_valid_floor(new_floors):
                    continue

                s = floor_to_str(new_floors, l, step + 1)
                if s[:_LEN] in cache:
                    continue

                stack.append(s)
                cache.add(s[:_LEN])

    idx += 1

print(step)
