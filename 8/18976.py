from itertools import *
from string import printable
c = 0
for x in product(str(printable[:20]), repeat=5):
    s = ''.join(x)
    fl = 1
    for i in range(len(s)-1):
        a = int(s[i], 20)
        b = int(s[i+1], 20)
        if (a%2 == b % 2) == 0:
            fl = 0
    if fl:
        if int(s[0], 20) + int(s[-1], 20) == 26:
            c += 1
print(c)