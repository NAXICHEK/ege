from itertools import product, repeat
from string import printable
print(printable[:12])
c = 0
for x in product(printable[:12], repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('7') == 1:
            if s.count('9')+s.count('a')+s.count('b') <= 3:
                c += 1
print(c)