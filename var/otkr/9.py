f = open('9')
c = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if len(set(a)) == len(a):
        if a[-1] + a[-2] <= a[-3] + a[-4] + a[-5]:
            c += 1
print(c)