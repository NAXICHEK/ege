from sys import setrecursionlimit

setrecursionlimit(9999)

def f(n):
    if n >=7 and n % 3 != 0: return 5 - f(n-1)
    if n >= 7 and n % 3 == 0: return 3 + f(n-1)
    return 7
print(f(3015))