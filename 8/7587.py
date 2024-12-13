from  itertools import *
c = 1
for x in product('АВЛОР', repeat = 4):
    s = ''.join(x)
    if s[0] == 'Л':
        print(c) # 251
        break
    c += 1