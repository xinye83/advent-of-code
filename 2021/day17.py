data = open("input/day17_ex.in", "r").read().strip("\n")
data = data[13:].split(",")
x1, x2 = data[0][2:].split("..")
y1, y2 = data[1][2:].split("..")

# cannot reach for sure if x > x2 or y < y1
#
