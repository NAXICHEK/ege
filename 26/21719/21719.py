f = open('26_21719.txt')
n = f.readline()
g = []
for i in f:
    a, b = i.split()
    g.append([int(a), int(b)])
dj_arbuz = []
for i in g:
    a, b = i
    d = set()
    d.add(a)
    for j in g:
        aa, bb = j
        if a == aa:
            d.add(bb)
    dj_arbuz.append(list(d))
    print(1)
print(dj_arbuz)