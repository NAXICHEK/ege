from itertools import product, repeat
from string import printable
c = 0
for x in product(printable[:10], repeat=4):
    s = ''.join(x)
    if s[0] != '0':
        if len(list(s)) == len(set(s)):
            for i in s:
                i = int(i)
                if i % 2 == 0:
                    s = s.replace(f'{i}', '!')
                elif i % 2 == 1:
                    s = s.replace(f'{i}', '?')
                else: pass
            if ('!!' not in s) and ('??' not in s):
                c += 1
print(c)