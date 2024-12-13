from math import *
for a in range(1, 100000):
    kod = ceil(log2(a))
    chad = ceil(23*kod/8)
    if 500000*chad <= 21*1024*1024:
        print(a)