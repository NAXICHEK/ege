from itertools import product, repeat
from string import printable
from time import process_time
import sys
p = []
v = []

def f(x, g):
    s = ''
    while x > 0:
        s = str(x%g) + s
        x //= g
    return s

for x in product(printable[:16], repeat=7):
    s = ''.join(x)
    if s[4] == 'a':
        p.append(s)
        print(s)
print(1, process_time())
for x in product(printable[:8], repeat=9):
    s = ''.join(x)
    if s[4] == '2':
        if s[-1] == '3':
            v.append(s)
print(2, process_time())
for i in p:
    for j in v:
        i = f(i, 16)
        j = f(j, 8)
        if i == j:
            print(i, process_time())