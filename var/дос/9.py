f = open('9')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a3 = [x for x in a if a.count(x) == 3]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 6 and len(a1) == 1:
        if max(a3) > a1[0]:
            c += 1
            print(a)
print(c)