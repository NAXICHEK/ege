from math import *
for i in range(1, 10000):
    a1 = 26
    a2 = 1984
    kod1 = ceil(log2(a1))
    kod2 = ceil(log2(a2))
    chad1 = 5*kod1/8
    chad2 = 90*kod2/8
    obschad = chad1 + chad2
    if (obschad + i) * 32768 < 5*1024*1024:
        print(i, (i+obschad)*32768, 5*1024*1024)