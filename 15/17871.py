def p(x):
    return 15 <= x <= 40

def q(x):
    return 21 <= x <= 61

def f(a, x, b):
    return a <= x <= b
m = 1000000
for a in range(100):
    for b in range(100):
        fl = 1
        for x in range(1000):
            if (p(x) <= ((q(x) and (not f(a, x, b))) <= (not p(x)))) == 0:
                fl = 0
        if fl:
            m = min(b-a, m)
print(m) # 19