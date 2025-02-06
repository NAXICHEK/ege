from itertools import *
f = open('24.12_19719.txt').readline()
for i in range(10, 1, -1):
    for x in product('*-', repeat=i):
        s = ''.join(x)
        if s in f:
            f = f.replace(s, '.')
c = 0
g = '12349'
for i in g:
    f = f.replace(i, '1')
print(f)
for i in range(10, 0, -1):
    s = '.' + '0' * i
    s1 = '*' + '0' * i
    s2 = '-' + '0' * i
    if s in f:
        f = f.replace(s, '.')
    if s1 in f:
        f = f.replace(s, '*')
    if s2 in f:
        f = f.replace(s, '-')
print(f)