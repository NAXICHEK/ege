from math import *
for i in range(1, 100000000000000000):
    a = i
    kod = ceil(log2(a))
    chad = ceil(kod*261/8)
    if chad*252500/1024/1024 >= 31:
        print(i)
        break