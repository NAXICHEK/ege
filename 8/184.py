from itertools import *
c = 0
for x in product('ТОК', repeat=6):
    s = ''.join(x)
    if s[0] == 'Т' or s[0] == 'К':
        c += 1
print(c)