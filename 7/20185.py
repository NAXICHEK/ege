from math import log2
for i in range(100000):
    a = 6580*3240 * log2(2048)
    if a*i <= 3964685 * 8 * 510:
        print(i)