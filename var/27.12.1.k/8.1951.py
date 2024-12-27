from itertools import *
c = 0
cc = 0
for x in product(sorted('ПЛЮСЁНОК'), repeat=7):
    s = ''.join(x)
    for y in 'ПЛСНК': s = s.replace(y, 'С')
    if s[0] != 'С' and 'СЁ' not in s and 'ЁС' not in s:
        c += 1
    # if s[0] != 'П' and s[0] != 'Л' and s[0] != 'С' and s[0] != 'Н' and s[0] != 'К':
    #     if ('ПЁ' not in s) and ('ЁП' not in s) and ('ЛЁ' not in s) and ('ЁЛ' not in s) and ('СЁ' not in s) and ('ЁС' not in s) and ('НЁ' not in s) and ('ЁН' not in s) and ('КЁ' not in s) and ('ЁК' not in s):
    #         cc += 1
print(c, cc)