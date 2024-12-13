def div(x):
    d = set()
    for i in range(2, int(x ** 0.5 + 1)):  # если не нужно включать само число, то в рендже вместо 1 ставим 2
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
for x in range(550000, 10054043+1):
    d = div(x)
    if len(d) > 0:
        f = sum(d) // len(d)
        if f % 31 == 13:
            print(x, f)

