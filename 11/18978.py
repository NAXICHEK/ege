from math import *
c = 0
for i in range(1, 10000):
    a = i
    kod = ceil(log2(a))
    chad = ceil(kod*312/8)
    if 51 * 1024 * 1024 <= chad*125700 <= 52 * 1024 * 1024:
        print(i)
        c += 1
print(c)