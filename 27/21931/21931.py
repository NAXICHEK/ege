

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def anc(cluster):
    minimalki = []
    for i in cluster:
        summ = 0
        for j in cluster:
            d = dist(i, j)
            if d != 0:
                summ += d
        minimalki.append([i, summ])
    m = 0
    for i in minimalki:
        m = max(m, i[1])
    for i in minimalki:
        if i[1] == m:
            return i

f = open('27_A_21931.txt')
g = []
for i in f:
    i = i.split('\t')
    for j in range(len(i)-1):
        g.append([float(i[j].replace(',', '.')), float(i[j+1].replace(',', '.'))])
pc = []
vc = []
for i in g:
    x, y = i
    if y >= 10: pc.append(i)
    else: vc.append(i)
a1 = anc(pc)
a2 = anc(vc)
print(a1)
print(a2)
print(int((a1[0][0]+a2[0][0])/2*10000))