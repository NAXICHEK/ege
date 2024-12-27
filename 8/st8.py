from itertools import *
c = 0
for i in range(7):
    for x in product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=i):
        s = ''.join(x)
        if s == 'FEDABC':
            print(c)
        c += 1
print(c)