from itertools import *
c = 0
for x in product('0123456789abcdefghij', repeat=5):
    s = ''.join(x)
    fl = 1
    for i in range(len(s)-1):
        if (int(s[i], 20) % 2 == int(s[i+1], 20) % 2) == 0:
                fl = 0
    if fl:
        if int(s[0], 20) + int(s[-1], 20) == 26:
            c += 1

print(c)