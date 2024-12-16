from math import *
for i in range(1000):
    i = i/10
    a = (1536*1024*log2(4096))*150
    if a*i == (288*1024*8)*60*4:
        print(1-i) #  на 80%