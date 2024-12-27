f = lambda j,we,k: j <= we <= k
m = 1000000000
for a in range(100):
    for b in range(100):
        fl = 1
        for x in range(1000):
            if (((not f(10, x, 45)) <= f(35, x, 78)) and (not f(a, x, b))) == 1:
                fl = 0
        if fl:
            m = min(m, b-a)
print(m)