f = open('17.txt')
g = [int(x) for x in f]
m = min([x for x in g if str(x)[-1]=='6'])
c = 0
mikky = 0
for i in range(len(g)-1):
    a = g[i]
    b = g[i+1]
    if (str(a)[-1] == '6') or (str(b)[-1] == '6'):
        if a**2 + b**2 < m**2:
            c += 1
            mikky = max(mikky, a**2 + b**2)
print(c, mikky)