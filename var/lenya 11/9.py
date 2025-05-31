f = open('9')
for s in f:
    n = 0
    d = 0
    s = s.replace('\t', ' ')
    a = sorted([int(x) for x in s.split(' ')])
    a1 = [x for x in a if a.count(x) > 1]
    print(a, 'a')
    print(a1, 'a1')
    if a1: continue
    else:
        print(1)
        for i in a:
            if i % 2 == 0:
                d += i
            else:
                n += i**3
        if d**2 > n:
            print(sum(a))