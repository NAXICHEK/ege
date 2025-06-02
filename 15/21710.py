def f(a, x, b):
    return b >= x >= a
m = 1000000
for a in range(200):
    for b in range(200):
        fl = 1
        for x in range(10000):
            if ((not f(a, x, b)) <= (f(36, x, 75) == f(60, x, 110))) == 0:
                fl = 0
                break
        if fl:
            m = min(b-a, m)
print(m) # 74