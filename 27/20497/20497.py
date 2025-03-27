from math import *

from aiohttp.hdrs import PRAGMA

f = open('27.19.A_20497-2.txt')
g = [x[:-1].replace(',', '.') for x in f]
def cent(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

pc = []
vc = []
tc = []
pcd = []
vcd = []
tcd = []
m1 = 10000000000
m2 = 10000000000
m3 = 10000000000
otv = []
for i in g:
    x, y = i.split()
    x, y = float(x), float(y)
    if (-1 < x < 1.5) and (1 < y < 6.2):
        pc.append([x, y])
    elif (-3 < x < 0) and (-5 < y < 0.1):
        vc.append([x, y])
    elif (0.5 < x < 3.2) and (-5 < y < 0.1):
        tc.append([x, y])
print(len(g)-len(pc)-len(vc)-len(tc))
for i in pc:
    r = 0
    for j in pc:
        d = cent(i, j)
        if d != 0:
            r += d
    pcd.append([i, r])

for i in pcd:
    m1 = min(m1, i[1])

for i in vc:
    r = 0
    for j in vc:
        d = cent(i, j)
        if d != 0:
            r += d
    vcd.append([i, r])

for i in vcd:
    m2 = min(m2, i[1])

for i in tc:
    r = 0
    for j in tc:
        d = cent(i, j)
        if d != 0:
            r += d
    tcd.append([i, r])

for i in tcd:
    m3 = min(m3, i[1])

for i in pcd:
    if i[1] == m1:
        otv.append(i)

for i in vcd:
    if i[1] == m2:
        otv.append(i)

for i in tcd:
    if i[1] == m3:
        otv.append(i)
print(otv)
print('A:', floor((0.3250248483648603-1.5198997418306133+1.809550273615512)/3*10000))