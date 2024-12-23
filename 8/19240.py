from itertools import *
c = 1
for x in product(sorted('ЯНВАРЬ'), repeat=5):
    s = ''.join(x)
    if s[0] != 'Я' and s.count('Ь') < 2 and 'ЯЯ' not in s:
        print(c)
    c += 1
