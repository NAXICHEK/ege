f = open('9')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    a3 = [int(x) for x in a if a.count(x) == 3]
    a1 = [int(x) for x in a if a.count(x) == 1]
    if (len(a3) == 3) and (len(a1) == 3):
        if sum(a3)**2 > sum(a1)**2:
            c += 1
print(c)