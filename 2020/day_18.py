# --- Day 18: Operation Order ---

data = open("input/day_18.in", "r").read().strip("\n").split("\n")

# --- part 1 ---

# solution from geohotz
# https://www.youtube.com/watch?v=OxDp11u-GUo&t=1115s


class Number1:
    def __init__(self, num):
        self.num = num

    def __add__(self, x):
        return Number1(self.num + x.num)

    def __sub__(self, x):
        return Number1(self.num * x.num)


def evaluate1(string):

    s = ""
    is_number = False

    for c in string:
        if c in "0123456789" and not is_number:
            s += "Number1("
            is_number = True
        elif c not in "0123456789" and is_number:
            s += ")"
            is_number = False

        s += c

    if is_number:
        s += ")"

    return eval(s).num


sum = 0

for line in data:
    sum += evaluate1(line.replace("*", "-"))

print(sum)

# --- part 2 ---


class Number2:
    def __init__(self, num):
        self.num = num

    def __add__(self, x):
        return Number2(self.num * x.num)

    def __mul__(self, x):
        return Number2(self.num + x.num)


def evaluate2(string):

    s = ""
    is_number = False

    for c in string:
        if c in "0123456789" and not is_number:
            s += "Number2("
            is_number = True
        elif c not in "0123456789" and is_number:
            s += ")"
            is_number = False

        s += c

    if is_number:
        s += ")"

    return eval(s).num


sum = 0

for line in data:
    sum += evaluate2(line.replace("+", "-").replace("*", "+").replace("-", "*"))

print(sum)
