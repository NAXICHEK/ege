from itertools import *
c = 0
for x in product(sorted('АКЛМНЯ'), repeat = 5):
    c += 1
    s = ''.join(x)
    if s[0:2] == 'КМ':
        print(c)
        break # 1945