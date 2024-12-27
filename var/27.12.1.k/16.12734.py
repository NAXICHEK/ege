from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 52: return n
    return 3 * f(n-2) - n

for i in range(100000):
    f(i)
print(f(15127)//f(15099))