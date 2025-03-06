from math import *
for i in range(1000):
    a = 640*480 * (log2(64) + i)
    if a <= 600*1024*8:
        print(2**i)