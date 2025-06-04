f = open('26_2480.txt')
n = f.readline()
g = set()
for i in f:
    a, b = i.split()
    a, b = int(a), int(b)
    for j in range(a+1, b-1):
        g.add(j)
print(g)
c = 0
g = list(g)
m = 0
for i in range(len(g)-1):
    a = g[i]; b = g[i+1]
    if b-a != 1:
        m = max(m, b-a)
        c += b-a
print(m, c)