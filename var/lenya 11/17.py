f = open('17_21990.txt').read()
f = f.replace('\n', ' ')
f = f.split(' ')
g = []
for i in f:
    if i != '':
        g.append(int(i))
maxi = max(g)
for i in range(len(g)-2):
    a = g[i]; b = g[i+1]; c = g[i+2]
