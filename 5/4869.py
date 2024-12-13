from math import *
a = []

for i in range(2, 10000):
    b = bin(i)[2:]
    c = 1
    e = 0
    n = 0
    for gey in b:
        if (gey == '1') and (c % 2 == 0):
            e += 1
        if (gey == '0') and (c % 2 == 1):
            n += 1
        c += 1
    r = abs(e - n)
    if r == 5:
        a.append(i)
print(min(a))