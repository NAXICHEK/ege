from itertools import *
from string import printable
c = 0
for x in product(printable[:12], repeat=5):
    s = ''.join(x)
    d = 0
    print(s)
    if s[0] != '0':
        for i in range(len(s)-1):
            if int(s[i], 12) % 2 != 0 and int(s[i+1], 12) % 2 != 0:
                d += 1
        if d <= 2:
            c += 1
print(c)