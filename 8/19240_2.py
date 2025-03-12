from itertools import *
c = 1
for x in product(sorted('ЯНВАРЬ'), repeat=5):
    s = ''.join(x)
    if s[0] != 'Я':
        if s.count('Ь') <= 1:
            if 'ЯЯ' not in s:
                print(c)
    c += 1