f = open('19481.txt')
c = 1
cc = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    aa = [x for x in a if a.count(x) > 1]
    if len(aa) == 0:
        if (a[0] + a[3])**2 > a[1]**3 + a[2]**3:
            cc += c
    c += 1

print(cc)