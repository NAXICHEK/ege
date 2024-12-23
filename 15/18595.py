f = lambda a, x, b : a <= x <= b
m = 0
for a in range(100):
    for b in range(200):
        fl = 1
        for x in range(1, 1000):
            if ((not (f(48, x, 94) or f(83, x, 100))) <= (not (f(a, x, b)))) == 0:
                fl = 0
        if fl:
            m = max(m, b-a)
print(m)
