from math import *

a = 1550 + 10
kod = ceil(log2(a))
chad = ceil(196 * kod / 8)
for i in range(100000):
    if (chad + i) * 2048 == 604 * 1024:
        print(i)