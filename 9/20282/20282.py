f = open('20282.txt')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    b = []
    if a[0]**2 + a[5]**2 >= (a[1] + a[2] + a[3] + a[4])**2:
        for i in a:
            b.append(a.count(i))
        if 3 in b and 2 not in b:
            c += 1
print(c)