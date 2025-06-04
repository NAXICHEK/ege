from time import *
f = open('24_19254.txt').read()
t = time()
f = f.split('FSRQ')
m = 0
h = 0
for i in range(len(f)):
    d = len(f[i])
    a = []
    for j in range(i+1, len(f)):
        d += len(f[j])
        if j-i == 82:
            break
        a.append(d)
    print(m, d, len(a), len(a)*4+d, a)
    m = max(m, len(a[2:-2])*4+d-h-1)
    h = len(f[i])
print(m, time()-t)