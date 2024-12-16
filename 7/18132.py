from math import *
for i in range(10000):
    a = (i * 768 * ceil(log2(4000))) * 50
    if a <= 300 * 1310720:
        print(i) # 853