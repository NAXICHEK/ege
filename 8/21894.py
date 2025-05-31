from itertools import product
from string import printable

c = 0
for x in product(printable[:10], repeat=4):
    s = ''.join(x)
    if s[0] != '0':
        if len(s) == len(set(s)):
            for i in s:
                if int(i) % 2 == 0:
                    s = s.replace(i, '!')
                else:
                    s = s.replace(i, '@')
            if '!!' not in s:
                if '@@' not in s:
                    c += 1
print(c)