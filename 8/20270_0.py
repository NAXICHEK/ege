from itertools import *
from string import printable
c = 0
a = []
for x in product('0246', repeat=3):
    s = ''.join(x)
    print(s)
    a.append(s)
for x in product(printable[:7], repeat=5):
    s = ''.join(x)
    d = True
    b = 0
    if s[0] != '0':
        for j in a:
            if j in s:
                d = False
        if d:
            for i in range(len(s)-1):
                if int(s[i], 7) % 2 == 0 and int(s[i+1], 7) % 2 == 0:
                    b += 1
        if b >= 2:
            c += 1
print(c)