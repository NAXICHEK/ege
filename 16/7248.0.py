from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0: return 1
    if n%2 == 1: return f(n//10) * (n%10)
    return f(n//10)

c = 0
# g = [int(x) for x in range(10**9, 10**10+1) if str(x)[-1] == '0' or str(x)[-1] == '1' or str(x)[-1] == '2' or str(x)[-1] == '4' or str(x)[-1] == '6' or str(x)[-1] == '7' or str(x)[-1] == '8']
# 0 1 2 4 6 7 8

for i in range(10**9, 10**10+1):
    a = f(i)

    if a == 49:
        c += 1
        print(c, i)
print(c)