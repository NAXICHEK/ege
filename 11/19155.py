from math import *
c = 0
for i in range(1, 10000):
    a = i
    kod = ceil(log2(a))
    chad = ceil(kod*157/8)
    if 30*1024*1024 <= chad*233700 <= 31*1024*1024:
        c += 1
        print(i)
print(c)