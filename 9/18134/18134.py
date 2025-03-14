f = open('18134')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a2 = [x for x in a if a.count(x) == 2]
    am = [x for x in a if a.count(x) == 1]
    if len(a2)/2 == 2 and len(am) == 2:
        if a2[-1]**2 > (am[0]*am[1]):
            print(a, a2, am, a[-1]**2, (am[0]*am[1]))
            c += 1
print(c)