from string import *
from itertools import *
from time import process_time
c = 0
for x in product(printable[:9], repeat = 9):
    a = []
    b = []
    d = 0
    s = ''.join(x)
    fl = 1
    for i in range(len(s)-1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                fl = 0
                if fl == 0:
                    break
    if fl == 1 and s.count('0') == 0:
        if s.count('1') < 4 and s.count('2') < 4 and s.count('3') < 4 and s.count('4') < 4 and s.count('5') < 4 and s.count('6') < 4 and s.count('7') < 4 and s.count('8') < 4:
            c += 1
            print(c)
print(c, process_time())