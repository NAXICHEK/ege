from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(999999)
@lru_cache(None)
def f(n):
    if n <= 1: return 1
    if n > 1 and n % 3 == 0: return n + f(n/3)
    if n > 1 and n % 3 == 1: return n + f(n+3)
for i in range(1000000000000000000):
    f(i)

a = []
for n in range(10000):
    try:
        if f(n) > 100: a.append(n)
    except TypeError:
        print(0)
print(min(a))