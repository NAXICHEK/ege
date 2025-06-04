f = open('9')
c = 0
for s in f:
    c += 1
    a = [int(x) for x in s.split()]
    a3 = {x for x in a if a.count(x) == 3}
    aa = [x for x in a if a.count(x) > 0]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 2:
        if sum(aa)//len(aa) < a1[0]:
            print(c)