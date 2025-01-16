f = open('24_18029.txt').read()
f = f.replace('Y', '-')
f = f.replace('Z', ',')
f = f.replace('X', ' ').split()
m = 0
g = []
for i in f:
    g.append([i.count('-'), len(i)+2])
for i in g:
    a = i[0]
    m = max(m, a)
for i in g:
    if i[0] == m:
        print(i[1])