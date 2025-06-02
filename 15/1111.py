def f(a, x, b):
    return b >= x >= a
m = 10000000
for a in range(100):
    for b in range(100):
        fl = 1
        for x in range(1000):
            if ((((not f(19, x, 80)) <= (f(13, x, 31) or f(48, x, 114)))) <= ((not f(a, x, b)) <= (not f(19, x, 80)))) == 0:
                fl = 0
                break
        if fl:
            m = min(m, b-a)
print(m)