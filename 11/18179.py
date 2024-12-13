from math import *
for i in range(1, 100000000000000000):
    a = i
    kod = ceil(log2(a))
    chad = ceil(kod*20/8)
    if chad*600000/1024/1024 >= 11:
        print(i)
        break