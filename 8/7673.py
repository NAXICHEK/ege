from itertools import *
c = 0
n = 0
k = 0
for x in product('ГЕЭ023', repeat = 7):
    s = ''.join(x)
    if s == 'ЕГЭ2023':
        n = c
    elif s == '2023ЕГЭ':
        k = c
    c += 1
print(k-n-1) # 166004