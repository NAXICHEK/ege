from itertools import *
c = 0

for x in product('0123456', repeat = 6):
    s = ''.join(x)
    fl = 0
    if s.count('6') == 1 and ((int(s[0]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[4]) % 2 == 0) and (int(s[1]) % 2 == 1 and int(s[3]) % 2 == 1 and int(s[5]) % 2 == 1)) or ((int(s[0]) % 2 == 1 and int(s[2]) % 2 == 1 and int(s[4]) % 2 == 1) and (int(s[1]) % 2 == 0 and int(s[3]) % 2 == 0 and int(s[5]) % 2 == 0)):
        c += 1
print(c)