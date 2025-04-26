from itertools import product, repeat
from string import printable
from time import process_time

p1 = []
p2 = []
v = []

for x in product(printable[:16], repeat=4):
    s = ''.join(x)
    p1.append(s)
for x in product(printable[:16], repeat=2):
    s = ''.join(x)
    p2.append(x)
for x in product(printable[:8], repeat=9):
    s = ''.join(x)



for i in p:
    for j in v:
        i = int(i, 16)
        j = int(j, 8)
        if i == j:
            print(i, process_time())