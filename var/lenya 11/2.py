from string import printable

s = '123'
from itertools import *
for x in product(printable[:17], repeat=6):
    s = ''.join(x)
    # for x in rang