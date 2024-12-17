from math import *
for i in range(1000):
    a = 1920*1080 * (i + ceil(log2(1500)) + 1)
    if a <= 4.5*1024*1024*8:
        print(2**i)