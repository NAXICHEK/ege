from itertools import *
n = []
c = 0
count = 0
for x in product('АКЛМНЯ', repeat = 5):
    s = ''.join(x)
    print(s)
    if s[0:2] == 'МН':
        n.append([s, c])
    c += 1
print(len(n)-2)