from functools import *
from time import process_time


@cache
def f(s, l):
    if l == 0: return f'{s:b}'.count('1') <= 1
    return sum(f(s ^ (1 << x), l-1) for x in range(8))

print((f(0, 27) - f(1, 26)) % (10**9+7), process_time())