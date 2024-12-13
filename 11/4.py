from math import *
for i in range(1, 1000000):
    a = 62 + i
    kod = ceil(log2(a))
    chad = ceil(kod*24/8)
    if chad * 5100 < 170*1024:
        print(i)