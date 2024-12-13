from math import *
a = 26 + 10 + 450
kod = ceil(log2(a))

for i in range(1000):
    chad = i * kod/8
    if chad*575 > 100*1024:
        print(i)
        break