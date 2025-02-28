f = open('17863')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x) == 1]
    a3 = [x for x in a if a.count(x) == 3]
    if len(a1) == len(a3):
        if sum(a1)**2 < sum(a3)**2:
            c += 1
print(c)