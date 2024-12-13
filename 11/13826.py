from math import *

for i in range(1000):
    a1 = 26
    a2 = 5000
    kod1 = ceil(log2(a1))
    kod2 = ceil(log2(a2))
    chad1 = ceil(10 * kod1)
    chad2 = kod2
    obs = ceil((chad1 + chad2) / 8)
    if (obs + i) * 30 == 1500:
        print(i)