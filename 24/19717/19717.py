f = open('24.5_19717.txt').readline()
f = f.split('M')
a = []
b = []
c = []
d = 0
for i in f:
    a.append(len(i))
try:
    for i in range(len(a)):
        d = 0
        for j in range(i, i + 279):
            b.append(a[j])
        for h in b:
            d += h
        c.append(d)
        b.clear()
except IndexError: pass
print(max(c))   