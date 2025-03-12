from itertools import *
c = 0
for x in set(permutations('ПАРИЖАНКА')):
    s = ''.join(x)
    s = s.replace('А', '?').replace('И', '?')
    d = 0
    for i in range(len(s) - 1):
        if s[i] == '?' and s[i+1] == '?':
            d += 1
    if d == 1:
        c += 1
print(c)