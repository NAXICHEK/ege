from itertools import *
c = 0
for x in product(sorted('МЫСЛЬ'), repeat = 5):
    c += 1
    s = ''.join(x)
    if s[0:2] == 'ЫЫ':
        print(c) # 2374