# Определите количество 12-ричных шестизначных чисел, в записи которых содержится ровно одна цифра «B»
# и равное количество чётных и нечётных цифр
from itertools import *
from string import printable
c = 0
for x in product(printable[:12], repeat=6):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('b') == 1:
            ch = 0
            nch = 0
            for i in s:
                if int(i, 12) % 2 == 0: ch += 1
                else: nch += 1
            if ch == nch:
                c += 1
print(c)