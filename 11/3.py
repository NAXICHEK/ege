from math import *
for i in range(1, 1000):
    a = 62 + i
    kod = ceil(log2(a))
    chad = ceil(kod*30/8)
    if chad * 4700 < 180*1024:
        print(i)