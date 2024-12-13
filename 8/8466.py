from itertools import *
c = 0
for x in product('0123456', repeat = 6):
    s = ''.join(x)
    if (s[-1] == '6' or s[-1] == '5' or s[-1] == '4') and (s[0] != '0'):
        if s.count('0') + s.count('2') + s.count('4') + s.count('6') == s.count('1') + s.count('3') + s.count('5'):
            c += 1
print(c)