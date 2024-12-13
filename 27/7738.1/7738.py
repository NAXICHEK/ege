from turtle import *

f = open('27-63b.txt')

data = []

for l in f:
    s = l.strip().replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append(p)

print(len(data))

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def get_cluster(p0):
    odin_cl = [p for p in data if dist(p0, p) < 0.3]
    if len(odin_cl) > 0:
        for p in odin_cl:
            data.remove(p)
    next_cl = [get_cluster(p) for p in odin_cl]
    odin_cl = odin_cl + [i for s in next_cl for i in s]
    return odin_cl

clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + get_cluster(p0)
    print(len(cluster))
    clusters.append(cluster)

k = len(clusters)

def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]

centroid = [center(kl) for kl in clusters]
print(centroid)

px = sum(x for x, y in centroid)
py = sum(y for x, y in centroid)

print(int(px/k*100000), int(py/k*100000))

tracer(0)
colors = ['red', 'green', 'blue'] + ['black'] * (k-3)
screensize(3000, 3000)
for kl, color in zip(clusters, colors):
    up()
    for x, y in kl:
        goto(x*40, y*40)
        dot(3, color)
update()
done()