from itertools import product
from string import *
c = 0
for x in product(printable[:17], repeat=6):
    s = ''.join(x)
    if s[0] != '0':
        if len(s) == len(set(s)):
            for i in s:
                if int(i, 17) % 2 == 0:
                    s = s.replace(i, '!')
                else:
                    s = s.replace(i, '@')
            if '!!!' not in s:
                if '@@@' not in s:
                    c += 1
print(c)