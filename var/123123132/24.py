from time import *
f = open('24_19254.txt').read()
t = time()
m = 0
for i in range(len(f)):
    for j in range(i+1, len(f)):
        s = f[i:j]
        if s.count('FSRQ') == 80:
            m = max(len(s), m)
            print(m)
print(m, time()-t)