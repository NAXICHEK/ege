from math import *
for i in range(1, 1000):
    a = i
    kod = ceil(log2(a))
    chad = ceil(kod*377/8)
    if chad*23155 >= 5536*1024:
        print(i)
        break