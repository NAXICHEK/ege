f = open('18594')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    ach = [x for x in a if x % 2 == 0]
    anch = [x for x in a if x % 2 != 0]
    if len(ach) == len(anch):
        if a[0]**2 <= sum(a)-a[0]:
            c += 1
print(c)