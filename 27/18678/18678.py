def dist(pc, vc):
    x1, y1 = pc
    x2, y2 = vc
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def cent(cluster):
    m = 10000000
    for i in cluster:
        d = 0
        for j in cluster:
            d += dist(i, j)
        m = min(m, d)
        if d == 190.46782548224272:
            return i
    return d
# [0.47707379734388755, 1.1522446502260968]
# [3.812544177066391, 3.838368711767422]
print((0.47707379734388755+3.812544177066391)/2*10000, (1.1522446502260968+3.838368711767422)/2*10000)
f = open('27A_18678.txt')
a = []
for i in f:
    a.append(i.replace(',', '.').split())

pc = []
vc = []
an = 0

for i in a:
    x, y = i
    x = float(x)
    y = float(y)
    if y <= 2.5:
        pc.append([x, y])
    elif (y >= 2.5) and (x >= 1.2) and (x <= 6.3):
        vc.append([x, y])
    else: an += 1
print(cent(vc))