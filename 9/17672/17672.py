c = 0
f = open('17672')
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[0] + a[-1] < sum(a) - (a[0] + a[-1]):
        c += 1
print(c)