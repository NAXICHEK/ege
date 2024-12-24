from itertools import permutations, repeat, product

c = 0
for x in product('ВЬЮГА', repeat=6):
    s = ''.join(x)
    if 'ЮГ' in s:
        c += 1
print(c)