from sys import setrecursionlimit

setrecursionlimit(999999)

def f(n):
    if n == 1: return 1
    if n > 1: return 2 * n + f(n-1)
print(sum(map(int, str(f(57693))))**2)