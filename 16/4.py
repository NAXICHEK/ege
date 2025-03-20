from functools import lru_cache
from time import process_time


@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return (n-1)*(f(n-1))

for i in range(2200):
    f(i)

print((f(2024) + 2 * f(2023)) / f(2022))