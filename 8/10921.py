from itertools import *
from time import process_time
c = 0
for x in set(permutations('ДЖАВАСКРИПТ', 11)): # ПОЧЕМУ ТУТ СЕТ?????
    s = ''.join(x)
    for j in s:
        if j == 'А' or j == 'И':
            pass
        else: s = s.replace(j, '.')
    d = 0
    for i in s:
        if i != '.':
            d += s.index(f'{i}') + 1
            s = s.replace(i, '.', 1)
    if d == 11:
        c += 1
        print(c)
print(c)
