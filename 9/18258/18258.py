f = open('18258')
c = 0
for s in f:
    c += 1
    a = [int(x) for x in s.split()]
    aa = sorted([x for x in a])
    b = [x for x in aa if aa.count(x) > 1]
    if a == aa:
        for i in b:
            if sum(map(int, str(i))) % 2 == 0:
                print(c)