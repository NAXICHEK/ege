from itertools import *
from string import printable
c = 1
for x in product(sorted('кодим'), repeat=5):
    s = ''.join(x)
    if s.count('м') == 2 and 'мм' not in s:
        print(c)
    c += 1
