f = open('26_20815.txt')
f.readline()
n, k = 9996, 1076
g = []
for i in f:
    id, b1, b2, b3, s = i.split()
    g.append([int(id), int(b1)+int(b2)+int(b3), int(b1)+int(b2)+int(b3)+int(s), int(s)])
g = sorted(g, key=lambda x: x[2], reverse=True)
proshli = []
hh = 0
for i in range(k+30):
    m = g[i][2]
    id = g[i][0]
    if m == 279:
        proshli.append(g[i])
        print(k-i)
    if k-i <= 2:
        print(id)
    hh += 1
print(sorted(proshli, key=lambda x: x[1]))