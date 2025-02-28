f = open('18924')
c = 0
cc = 0
for s in f:
    c += 1
    a = sorted([int(x) for x in s.split()])
    a3 = [x for x in a if a.count(x) == 3]
    ar = [x for x in a if a.count(x) > 1]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 3:
        d = 0
        for i in ar:
            d += i**2
        if d > sum(a1)**2:
            cc += 1
print(c - cc)