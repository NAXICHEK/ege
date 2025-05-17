f = open('17_21416.txt')
g = [int(x) for x in f]
cc = 0
su = sum(x for x in g if x <= -1)
m = 0
for i in range(len(g)-2):
    a = g[i]; b = g[i+1]; c = g[i+2]
    if max(a,b,c) * min(a,b,c) > su:
        cc += 1
        m = max(m, sum([a,b,c]))
print(cc, m)