from sys import *
from time import process_time
setrecursionlimit(999999999)
gamburger = ''
def f(n):
    if n == 0: return 6
    elif n > 0 and n % 2 == 0: return 1 + f(n / 2)
    else: return f(n // 2)
for i in range(1, 51):
    # if f(i) == 9:
    print(f(i))
    gamburger = gamburger + str(i) + '..'
print(len(gamburger), process_time(), gamburger)