f = open('7837')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x) == 1]
    print(a)
    print(a1)
    if len(a1) == 5:
        print(1)
        if (a[2]*2 > a[-1]) and (a[2]*2 > a[0] * 3):
            c += 1
print(c)