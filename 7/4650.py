from math import *
for i in range(1, 100000000000):
    a = 640*480 + 64 * i
    if a <= 600 * 1024 * 8:
        print(i)