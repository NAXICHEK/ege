from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 10: return n
    if n > 9: return 3 * n + g(n-2)
@lru_cache(None)
def g(n):
    if n < 10: return n
    if n > 9: return n - 2 + f(n-1)
for i in range(10000):
    f(i)
    g(i)
print(f(2204)-g(2200))