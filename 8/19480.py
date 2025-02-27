from itertools import product, permutations

c = 0
for x in set(permutations('ПАРИЖАНКА')):
    s = ''.join(x)
    s = s.replace('А', '!').replace('И', '!')
    if (s.count('!!') == 1) and ('!!!' not in s):
        c += 1
print(c)