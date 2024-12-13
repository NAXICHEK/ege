from math import *
for i in range(1000):
    a = 52 + 10 + i
    kod = ceil(log2(a))
    chad = ceil(53*kod/8)
    if 2000*chad <= 93*1024:
        print(i)