from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10: return n
    return f(n%10) + f(n//10)
c = 0
for i in range(2**63):
    d = f(i)
    if d == 159:
        c += 1
        print(c)
print(c, '1')