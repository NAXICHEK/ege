from itertools import product, repeat
from string import printable
c = 0
# 0123456789abcdef ghijklmno
print(printable[:25])
for x in product(printable[:25], repeat=4):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('0') + s.count('2') + s.count('4') + s.count('6') + s.count('8') + s.count('a') + s.count('c') + s.count('e') + s.count('g') + s.count('i') + s.count('k') + s.count('m') + s.count('0') == 1:
            if s.count('g') + s.count('h') + s.count('i') + s.count('j') + s.count('k') + s.count('l') + s.count('m') + s.count('n') + s.count('o') <= 2:
                c += 1
print(c)