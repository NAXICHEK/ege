from math import *
for i in range(1, 1000):
    a = i
    kod = ceil(log2(a))
    chad = ceil(35*kod/8) + 48
    if chad*1536 <= 120*1024:
        print(i)