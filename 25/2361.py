wdef div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for i in range(550000, 560000):
    d = [int(x) for x in div(i) if str(x)[-1:] == '7']
    if len(d) == 3:
        print(i, d[2])