from itertools import *
c = 0
for x in product(sorted('ЯНВАРЬ'), repeat=5):
    c += 1
    s = ''.join(x)
    if s[0] != 'Я':
        if s.count('Ь') <= 1:
            if 'ЯЯ' not in s:
                print(c)