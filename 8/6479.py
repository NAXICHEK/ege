from itertools import *
c = 0
for x in permutations('КАРПЫ'):
    s = ''.join(x)
    if ('АА' not in s) and ('ЫЫ' not in s) and ('АЫ' not in s) and ('ЫА' not in s):
        if s[0] != 'Р' and s[-1] != 'Р':
            c += 1
print(c)