from itertools import *
c = 0
for x in product(sorted('ПЛЮСЁНОК'), repeat=7):
    s = ''.join(x)
    if s[0] != 'П' or s[0] != 'Л' or s[0] != 'С' or s[0] != 'Н' or s[0] != 'К':
        if 'ПЁ' not in s and 'ЁП' not in s and 'ЛЁ' not in s and 'ЁЛ' not in s and 'СЁ' not in s and 'ЁС' not in s and 'НЁ' not in s and 'ЁН' not in s and 'КЁ' not in s and 'ЁК' not in s:
            c += 1
print(c)