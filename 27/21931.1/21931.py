f = open('27_A_21931.txt')
g = []
for i in f:
    i = i.replace(',', '.')
    a, b = i.split()
    g.append([float(a), float(b)])

from math import dist

def acentr(cl):
    m = []
    for p in cl:
        s = sum(dist(p,p1) for p1 in cl)
        m.append([s,p])
    return max(m)[1]

cl1 = []
cl2 = []

clusters = []
while g:
    cl = [g.pop()]
    for p in cl:
        sosed = [p1 for p1 in g if dist(p,p1)<1]
        for p1 in sosed:
            cl.append(p1)
            g.remove(p1)
    clusters.append(cl)

print([len(cl) for cl in clusters])
cl1 = clusters[0]
cl2 = clusters[1]
print(acentr(cl1))
print(acentr(cl2))
# for i in g:
#     x, y = i
#     if y >= 13: cl1.append(i)
#     else: cl2.append(i)

print((0.1663069+3.4435388)/2*1000)