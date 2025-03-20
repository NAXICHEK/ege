c = 0
f = open('12')
for s in f:
    a = sorted([int(x) for x in s.split()])
    a1 = [x for x in a if a.count(x) == 1]
    ab1 = [x for x in a if a.count(x) > 1]
    if a[-1] in a1:
        if ab1:
            if a[-1] > 3*(sum(a)- a[-1])/5:
                c += 1
print(c)
