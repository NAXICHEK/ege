from itertools import *
from string import printable
c = 0
for x in product(str(printable[:9]), repeat=7):
    s = ''.join(x)
    if s[0] != '0' and s[0] != '2' and s[0] != '4' and s[0] != '6':
        if s[-1] == s[-2] == s[-3]:
            pass
        else: c += 1
print(c)
