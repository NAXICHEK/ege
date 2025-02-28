f = open('18364')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    ar = [x for x in a if a.count(x) > 1]
    a1 = [x for x in a if a.count(x) == 1]
    if ar:
        g = 1
        for i in ar:
            g *= i
        if sum(a1)*3 <= g:
            c += 1
ц