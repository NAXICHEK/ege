from string import printable
from time import *
f = open('24_22359.txt').readline()
for i in printable[16:]:
    f = f.replace(i, '')
print(len(f))
t = time()
m = 0
for i in range(len(f)):
    for j in range(i+m, len(f)):
        s = f[i:j+1]
        # print(i, j)
        try:
            if int(s, 15) % 5 == 0:
                print(j, 11111111111111111111111111111111, time()-t)
                m = max(m, len(s))
            else:
                break
        except ValueError: pass