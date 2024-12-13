from sys import *
setrecursionlimit(9999)
def f(n):
    if n == 1: return 1
    else: return (2 * n - 1) * (f(n-1))
print(f(3516) / f(3513))