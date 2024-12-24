def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x//i}
    if len(d) > 0:
        return max(sorted(d))

from fnmatch import *
for i in range(23, 10**6, 23):
    gey = div(i)
    if fnmatch(str(gey), '#6215'):
        print(i, gey)