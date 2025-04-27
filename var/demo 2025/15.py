def p(x):
    return 15 <= x <= 40
def q(x):
    return 21 <= x <= 63
def a(n, x, k):
    return n <= x <= k
m = 1000
for n in range(100):
    for k in range(100):
        fl = 1
        for x in range(1000):
            if (p(x) <= ((q(x) and (not a(n, x, k))) <= (not p(x)))) == 0:
                fl = 0
        if fl:
            if k > n:
                m = min(m, k-n)
                print(k-n)
print(m)