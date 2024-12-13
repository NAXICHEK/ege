from math import *
for i in range(1, 1000):
    a = 52 + 10 + 963
    kod = ceil(log2(a))
    chad = ceil(i*kod/8)
    if 2000*chad <= 693*1024:
        print(i)