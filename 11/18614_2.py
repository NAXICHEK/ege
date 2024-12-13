from math import *
for i in range(100000):
    a = 52 + 10 + i
    kod = ceil(log2(a))
    chad = ceil(24 * kod / 8)
    if chad * 5100 <= 170*1024:
        print(i)