from itertools import product, repeat

c = 0
for x in product('ABCX', repeat=5):
    s = ''.join(x)
    if s[0] != 'X' and s[1] != 'X' and s[2] != 'X' and s[3] != 'X':
        c += 1
print(c)