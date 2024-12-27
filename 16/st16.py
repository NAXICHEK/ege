from functools import lru_cache


@lru_cache(None)
def f(n):
    if n % 2 == 0: return f(n/2) + 3
    if n % 2 != 0 and n % 3 == 0: return f(n/3) + 2
    if n % 2 != 0 and n % 3 != 0: return 0

for i in range(71):
    f(i)
    print(i)

print(f(70))