from math import *
for i in range(1, 100000000000000000):
    a = 52 + 10 + 450
    kod = ceil(log2(a))
    chad = ceil(kod*i/8)
    if chad*708/1024 >= 213:
        print(i)
        break