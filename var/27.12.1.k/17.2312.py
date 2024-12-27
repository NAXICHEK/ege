f = open('17_2312.txt')

g = [int(x) for x in f]
c = 0
m = 1000000

mini = min([int(x) for x in g if x % 2 != 0])
maxi = max([int(x) for x in g if x % 2 != 0])
sm = mini + maxi

for i in range(len(g)-1):
    a = g[i]
    b = g[i+1]
    if ((a+b) % 2 == 0) and ((a+b) > sm):
        c += 1
        m = min(m, a+b)
print(c, m)