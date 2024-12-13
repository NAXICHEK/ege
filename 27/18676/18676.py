from turtle import *
f = open('27B_18676.txt')
data = []

for line in f:
    s = line.strip().replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append(p)

print(len(data))

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_cluster(p0):
    odin_cl = [p for p in data if dist(p0, p) < 0.4]
    if len(odin_cl) > 0:
        for r in odin_cl:
            data.remove(r)
    next_cl = [get_cluster(g) for g in odin_cl]
    odin_cl = odin_cl + [item for sub in next_cl for item in sub]
    return odin_cl

clusters = []

while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    print(len(cluster))
    clusters.append(cluster)

k = len(clusters)
print(k)

def center(kl):
    m = []
    for p in kl:
        e = sum(dist(p, p1) for p1 in kl)
        m.append([e, p])
    return min(m)[1]

centroid = [center(kl) for kl in clusters]
print(centroid)

px = sum(x for x, y in centroid)
py = sum(y for x, y in centroid)

print(int(px/k*100000), int(py/k*100000))
# a 566258 38951
# b

tracer(0)
screensize(3000, 3000)
colors = ['red', 'green', 'blue'] + ['black']*(k-3)
for kl, color in zip(clusters, colors):
    up()
    for x, y in kl:
        goto(x*50, y*50)
        dot(3, color)
update()
done()