from itertools import *
c = 0
for x in product('АВОРТ', repeat = 6):
    s = ''.join(x)
    c += 1
    if s == 'ВОРОТА':
        print(c)