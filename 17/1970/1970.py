f = open('17.txt')
g = [int(i) for i in f]
m = max(i for i in g if abs(i) % 3 == 0)
c = 0
mah = 0
for i in range(len(g)-1):
    a, b = g[i], g[i+1]
    if (abs(a) % 3 == 0) or (abs(b) % 3 == 0):
        if a + b < m:
            c += 1
            mah = max(mah, a+b)
print(c)
print(mah)