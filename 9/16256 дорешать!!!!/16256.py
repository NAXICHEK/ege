f = open('16256')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x) == 1]

    if a1:
    