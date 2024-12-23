from sys import setrecursionlimit

setrecursionlimit(9999)
def f(n):
    if n > 3000: return n
    return (2*n+4) * f(n+2)
print(sum(map(int, str((int(f(20)/f(28)))))))