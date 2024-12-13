def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for i in range(300000, 400000):
    d = [int(x) for x in div(i) if x % 3 == 0]
    if len(d) == 5:
        print(i, d[4])