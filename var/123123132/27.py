f = open('27b')
g = []
for i in f:
    i = i.replace(',', '.')
    a, b = i.split()
    g.append([float(a), float(b)])

def rasstoynie(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def systema_poiska_centra_clusterov(cl):
    arbuz = []
    for i in cl:
        d = sum(rasstoynie(i, j) for j in cl)
        arbuz.append([d, i])
    return min(arbuz)[1]

cl1 = []
cl2 = []

for i in g:
    x, y = i
    if (y >= 6) and (x > 4) and (x < 5):
        cl1.append(i)
    else:
        cl2.append(i)
c1 = systema_poiska_centra_clusterov(cl1)
print(cl1)
c2 = systema_poiska_centra_clusterov(cl1)
print(abs(c1[0][0]+c2[0][0])/2*10000, abs(c1[0][1]+c2[0][1])/2*10000)