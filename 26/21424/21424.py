f = open('26_21424.txt')
n = int(f.readline())
g = sorted([int(x) for x in f])
for i in range(n):
    c = 1
    d = g[i]
    for j in range(i+1, n):
        if d + 9 <= g[j]:
            c += 1
            d = g[j]
    print(c, g[i]) # 1040 57