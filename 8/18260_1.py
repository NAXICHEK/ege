from itertools import *
c = 0
for x in product('0123456789ab', repeat=6):
    q = 0
    w = 0
    s = ''.join(x)
    if s[0] != '0':
        for i in s:
            if int(i, 12) % 2 == 0: q += 1
            else: w += 1
        if s.count('b') == 1 and w == q:
            c += 1
print(c)