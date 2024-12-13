from sys import *
from time import process_time
setrecursionlimit(9999)
def f(n):
    if n < 5:
        return 4**4
    if n > 4:
        return 4 * f(n - 4) + 4
print(f(4048) / f(4036), process_time())
