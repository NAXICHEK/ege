f = open('20488')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    p1 = [x for x in a if a.count(x) == 1]
    pm = [x for x in a if a.count(x) > 1]
    if p1:
        if pm:
            if a[-1] not in pm:
                if sum(p1) >= sum(pm)*3:
                    c += 1
print(c)