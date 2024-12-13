from turtle import *
f = open('27-57a.txt')
data = []

for l in f:
    s = l.strip().replace(',', '.')
    r = [float(p) for p in s.split()]
    data.append(r)
print(len(data))

def d(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def g_k(p0):
    od_k = [p for p in data if d(p0, p) < 1]
    if len(od_k) > 0:
        for p in od_k:
            data.remove(p)
    ne_kl = [g_k(p) for p in od_k]
    od_k = od_k + [i for s in ne_kl for i in s]
    return od_k

cluss = []
while len(data) > 0:
    p0 = data.pop
    cl = [p0] + g_k(p0)
    print(len(cl))
    cluss.append(cl)
k = len(cluss)
print(k)

def cent(kl):
    m = []
    for p in kl:
        s = sum()