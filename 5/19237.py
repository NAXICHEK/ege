from math import *

def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s
a = []
for i in range(1, 10000):
    n = f(i)
    if i % 3 == 0: n = n + n[-2:]
    if i % 3 != 0: n = n + f(sum(map(int, n)))
    r = int(n, 3)
    if r > 220 and r % 2 == 0:
        a.append(r)
print(min(a))