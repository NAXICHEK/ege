from itertools import *
c = 1
cc = 0
for x in product(sorted('престол'), repeat=5):
    s = ''.join(x)
    for y in 'прстл': s = s.replace(y, 'G')
    if (c % 2 != 0) and (s[-1] in 'ео') and (s.count('G') <= 3):
        cc += 1
    c += 1
print(cc)