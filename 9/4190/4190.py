f = open('4190')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0] + a[-1])**2 > a[1]**2 + a[2]**2 + a[3]**2:
        c += 1
print(c)