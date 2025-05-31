from itertools import *
from string import printable

c = 0
d = 0
for x in product(printable[:13], repeat=3):
    s = ''.join(x)
    if s[0] != '0':
        c += 1
        if str(c)[-1] == '7':
            for i in s:
                    if int(i, 13) % 2 == 1:
                        s = s.replace(i, '!')
            if '!!' not in s:
                d += 1
print(d, c)