from sys import setrecursionlimit

setrecursionlimit(999999)
def f(n):
    if n == 1: return 1
    if n > 1: return (n-1) * f(n-1)
print(288 * f(2023)//f(2022))