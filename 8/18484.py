from itertools import product, repeat
c = 0
for x in product(sorted('пвскаий'), repeat=6):
    s = ''.join(x)
    if 'аи' in s or 'иа' in s or 'аа' in s or 'ии' in s:
        c += 1
    if s == 'какааа':
        print(c)
