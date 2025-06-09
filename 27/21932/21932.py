f = open('27_A_21932.txt')
g = []
for i in f:
    i = i.replace(',', '.')
    a, b = i.split()
    g.append([float(a), float(b)])
from math import dist

def jestkiy_centr(cl):
    m = []
    for i in cl:
        s = sum(dist(i, j) for j in cl)
        m.append([s, i])
    return min(m)[1]
cl1 = []
cl2 = []
for i in g:
    x, y = i
    if y >= 12:
        cl1.append(i)
    else:
        cl2.append(i)

def dbscan(c,r):
    cl = []
    while c:
        cl.append([c.pop(0)])
        for j in cl[-1]:
            for i in c[:]:
                if dist(i,j) < r:
                    cl[-1].append(i)
                    c.remove(i)
    return cl

gey = dbscan(g, 2)
print(gey)
print(len(gey))
cl1 = gey[0]
cl2 = gey[1]
gey = jestkiy_centr(cl2)
pidor = jestkiy_centr(cl1)

print(int(gey[0]*10000))
print(int(pidor[1]*10000))