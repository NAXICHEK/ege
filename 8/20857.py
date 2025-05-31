from itertools import *
from string import printable
c = 1
for x in product(printable[:9], repeat=6):
    s = ''.join(x)
    c += 1
    if s[0] != '0':
        if str(c)[-1] == '5':
            for i in s:
                if int(i, 9) % 2 != 0:
                    s = s.replace(i, '!')
                if '!!' not in s:
                    print(s, c)