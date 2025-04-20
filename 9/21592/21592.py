c = 0
f = open('21592')
for s in f:
    c += 1
    a = sorted([int(x) for x in s.split()])
    ap = [x for x in a if a.count(x) == 2]
    a1 = [x**2 for x in a if a.count(x) == 1]
    if len(ap) / 2 == 3:
        if (ap[-1] - ap[0])**2 > sum(a1)*2:
            print(c)