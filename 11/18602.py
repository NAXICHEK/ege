from math import *
for i in range(1,10000):
    kod = ceil(log2(i))
    chad = ceil(kod*27/8)
    if chad*100000 >= 2 * 1024 * 1024:
        print(i)
        break