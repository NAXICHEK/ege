def cc(x):
    s = ''
    while x > 0:
        s = str(x%8) + s
        x //= 8
    return s
counter = 0
from itertools import *
g = []
for x in product('1357', repeat=2):
    s = ''.join(x)
    g.append(s)
for i in range(int('10000000000', 8), int('7'*11, 8)+1):
    a = cc(i)
    if len(a) == 11:
        if a.count('1') + a.count('3') + a.count('5') + a.count('7') == 3:
            c = 0
            for f in g:
                if f in a: c += 1
            if c == 0:
                counter += 1
                print(counter)
print(counter, '1')