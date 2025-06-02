from itertools import *
from string import printable
c = 0
for x in product(printable[:25], repeat=4):
    s = ''.join(x)
    if s[0] != '0':
        for i in s:
            if int(i, 25) % 2 == 1:
                s = s.replace(i, '!')
    if s.count('!') == 1:
        d = 0
        for i in s:
            if i != '!' and int(i, 25) <= 5:
                d += 1
        if d <= 2:
            c += 1
print(c)