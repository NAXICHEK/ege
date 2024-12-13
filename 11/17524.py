from math import *
a = 10 + 52 + 458
kod = ceil(log2(a))
for i in range(1,1000):
    chad = ceil(kod*i/8)
    if chad*862 <= 276*1024:
        print(i)
