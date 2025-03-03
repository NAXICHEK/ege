from pickle import PROTO

f = open('17_2312.txt')
g = [int(i) for i in f]
h = []
minn = 100000000000
maxx = 0
minnnn = 100000000000
for gey in g:
    if gey % 2 == 1:
        minn = min(minn, gey)
        maxx = max(maxx, gey)
c = 0
for i in range(len(g) - 1):
    if ((g[i] + g[i+1]) % 2 == 0) and (g[i] + g[i+1]) > (minn + maxx):
        c += 1
        minnnn = min(minnnn, g[i] + g[i+1])
print(c)
print(minnnn)