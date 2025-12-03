code16 = open("input/day16_ex.in", "r").read().strip("\n")
code2 = "".join([bin(int(c, 16))[2:].zfill(4) for c in code16])

print(code16)
print(code2)

def decode_bits(code, start, end):
    if start + 6 > end:
        return

    ver = int(code[start:start + 3], 2)
    tid = int(code[start + 3:start + 6], 2)

    if tid == 4: # leteral value
    else: # operator




# def sum_ver(code, start, end):
#     print(f"- {start} {end}")
#     if start >= end:
#         return 0

#     if start + 3 >= end:
#         return 0
#     ver = int(code[start: start + 3], 2)

#     if start + 6 >= end:
#         return 0
#     tid = code[start + 3: start + 6]

#     if tid == "100": # literal value

#         # find the end of this packet
#         temp = start + 6
#         while temp <= end:
#             if code[temp] == "0":
#                 break
#             temp += 5

#         return ver + sum_ver(code, min(end, temp + 1), end)
#     else: # operator
#         ltype = code[start + 6]

#         if ltype == "0":
#             # next 15 bits represents total length of the sub-packets
#             length = int(code[start + 7: start + 22], 2)

#             return ver + sum_ver(code, start + 22, start + 22 + length - 1) + sum_ver(code, start + 22 + length, end)
#         else:
#             # next 11bits represents number of the sub-packets
#             ver + sum_ver(code, start + 18, end)

# print(f"Part 1 - {sum_ver(code2, 0, len(code2) - 1)}")
