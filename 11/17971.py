from math import *
b = 26+28+10
char = ceil(log2(b))
arbuz = ceil((char * 12/8)+28)
for i in range(2,1000):
    a = arbuz * i
    if a >  20*1024:
        print(i-1)
        break