def pivo(x):
    d = set()
    for i in range(2, int(x ** 0.5 + 1)):  # если не нужно включать само число, то в рендже вместо 1 ставим 2
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
for x in range(150000, 1000000+1):
    d = pivo(x)
    a = sum(d)
    if a % 13 == 10:
        print(x, a)