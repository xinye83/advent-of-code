# --- Day 13: Shuttle Search ---

data = open("input/day_13.in", "r").read().strip("\n").split("\n")

# --- part 1 ---

import math

timestamp = int(data[0])

buses = data[1].replace("x,", "").split(",")
buses = [int(bus) for bus in buses]

minval = max(buses) ** 2

for bus in buses:
    minval = min((math.ceil(timestamp / bus) * bus - timestamp) * bus, minval)

print(minval)

# --- part 2 ---

"""
Chinese Remainder Theorem

Input:
	Both are lists of integers
		divisor   = [n_0, n_1, ..., n_k-1]
		remainder = [r_0, r_1, ..., r_k-1]

	(divisor has to be a coprime set)

Output:
	The smallest integer x that satisfies
		x % n_i = r_i for i = 0, 1, ..., k-1

Details:
	Let D = n_0 * n_1 * ... * n_k-1 and D_i = D / d_i, find a_i such that
		a_0 * D_0 + a_1 * D_1 + ... + a_k-1 * D_k-1 = 1
	then
		x % D = r_0 * a_0 * D_0 + r_1 * a_1 * D_1 + ... + r_k-1 * a_k-1 * D_k-1
"""

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce


def chinese_remainder(divisor, remainder):
    sum = 0
    prod = reduce(lambda remainder, b: remainder * b, divisor)
    for n_i, a_i in zip(divisor, remainder):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


divisor = []
remainder = []

temp = data[1].split(",")

# for bus b at position p on the list, the timestamp t satisfies
# 	t % b = -p % b

for i in range(len(temp)):
    if temp[i] != "x":
        divisor.append(int(temp[i]))
        remainder.append(-i % int(temp[i]))

print(chinese_remainder(divisor, remainder))
