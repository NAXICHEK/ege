from math import *
a = 10 + 2040
kod = ceil(log2(a))
print(kod)
chad = ceil(1000*kod/8)
print((chad*2**20)/1024/1024)