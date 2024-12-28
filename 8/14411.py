from itertools import *
c = 1
for x in product(sorted(set('СУБЛИМАЦИЯ')), repeat=5):
    s = ''.join(x)
    if c % 2 != 0:
        if s[-1] != 'Я':
            if s.count('У')+s.count('И')+s.count('А')+s.count('Я') == 2:
                print(c, s)
    c += 1