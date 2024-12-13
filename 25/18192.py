def div(n):
    d = set()
    for i in range(2, int(n ** 0.5 + 1)):  # если не нужно включать само число, то в рендже вместо 1 ставим 2
        if n % i != 0:
            d |= {i, n // i}
    return sorted(d)
for x in range(1000000, 1001000):
    d = div(x)
    if len(d) == 3:
        print(x)