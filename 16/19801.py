from functools import lru_cache
from time import process_time


@lru_cache(None)
def f(n):
    if n == 1: return 3
    if n > 1:
        return 5 * f(n-1)
for i in range(25**(5*10**11)):
    f(i)
print(process_time())

print(f((10**12 + 10)/(25**(5*10**11))), process_time())