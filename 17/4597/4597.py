f = open('17_4597.txt')
g = []
c = 0
m = 0
for s in f:
    s = s.replace('\n', '')
    g.append(int(s))
minn = min(g)
for i in range(len(g)-1):
    a = g[i]
    b = g[i+1]
    if (a % 117 == minn) or (b % 117 == minn):
        c += 1
        m = max(a+b, m)
print(c, m)