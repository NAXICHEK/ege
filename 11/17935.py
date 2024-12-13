from math import *
for i in range(1, 10000):
    a = 10 + 999
    kod = ceil(log2(a))
    chad = ceil(kod*745/8)
    if 312*(chad+i) <= 311*1024:
        print(312*i)