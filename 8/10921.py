from itertools import *
from time import process_time
c = 0
for x in set(permutations('ДЖАВАСКРИПТ')): # ПОЧЕМУ ТУТ СЕТ?????
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

# from itertools import permutations
# k = 0
# for i in set(permutations('ДЖАВАСКРИПТ', r=11)):
#     s = ''.join(i)
#     sumpos = 0
#     for j in range(len(s)):
#         if s[j]=='А' or s[j]=='И':
#             sumpos+=(j+1) #порядковый номер на единицу больше, чем индекс
#     if sumpos==11:
#         k+=1
# print(k, process_time())
