from itertools import *
from string import printable
c = 0
for x in product(printable[:5], repeat=9):
    s = ''.join(x)
    d = 0
    if s[0] != '0':
        s = s.replace('0', '?').replace('2', '?').replace('4', '?')
        for i in range(len(s)-1):
            if s[i] == '?' and s[i+1] == '?':
                d += 1
        if d == 2 and '???' not in s:
            c += 1
print(c)
