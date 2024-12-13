from math import *
a = 16 + 10
b = 100
kod = ceil(log2(a))
kod2 = ceil(log2(b))*2
print(kod2)
chad = ceil(((13*kod+kod2)/8))
print(chad)
for i in range(1, 101):
    if chad+i == 32:
        print(i, chad)