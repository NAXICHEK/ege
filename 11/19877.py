from math import *
for i in range(1000):
    a = ceil(log2(26))
    a1 = ceil(log2(1025))
    chad = (70*a1)/8
    chad1 = (4*a)/8
    if (chad1+chad+i)*131072 > 24*1024*1024:
        print(i)
        break