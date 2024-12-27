from itertools import *
from string import printable
c = 0
for x in product(str(printable[:12]), repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if (s.count('7') == 1 )and (s.count('9')+s.count('a')+s.count('b') <= 3):
            c += 1
            print(s)
print(c)