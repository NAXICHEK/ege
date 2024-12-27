from itertools import *
c = 1

# А Г Е М Н Р Т У

for x in product(sorted('АРГУМЕНТ'), repeat=4):
    d = 0
    s = ''.join(x)
    if len(s) == len(set(s)):
        for i in range(len(s)-1):
            if ord(s[i]) < ord(s[i+1]):
                d += 1
    if d == 3:
        print(c)
    c += 1