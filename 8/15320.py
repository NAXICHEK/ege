from itertools import *
c = 1
for x in product(sorted('ПАРУС'), repeat=5):
    s = ''.join(x)
    if s.count('У') < 2 and 'АА' not in s:
        print(c)
        break
    c += 1