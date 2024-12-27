from itertools import *
c = 0
for x in product('люстра', repeat=5):
    s = ''.join(x)
    if s.count('ю') <= 2:
        if s[-1] not in 'лстр':
            c += 1
print(c)