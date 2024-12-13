from math import *
a1, a2, a3 = 7, 19, 10

kod1 = ceil(log2(a1))
kod2 = ceil(log2(a2))
kod3 = ceil(log2(a3))

chad1 = ceil(1*kod1/8)
chad2 = ceil(10*kod2/8)
chad3 =  ceil(1*kod3/8)

obs = (chad1 + chad2 + chad3)

for i in range(100):
    if (obs + i) * 34 == 918:
        print(i)