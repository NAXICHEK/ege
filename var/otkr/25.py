def f(x):
    d = set()
    for i in range(1, int(x**0.5+1)):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)
c = 0
for i in range(500000, 100000000):
    r = sum(f(i))
    if str(r)[-1] == '6' and c != 5:
        print(i, r)
        c += 1