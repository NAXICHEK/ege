def div(x):
    d = set()
    for i in range(2, int(x ** 0.5 + 1)):  # если не нужно включать само число, то в рендже вместо 1 ставим 2
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
for x in range(250200, 15404003+1):
    d = div(x)
    if len(d) > 0:
        a = max(d)
        b = min(d)
        if (a + b) % 123 == 17:
            print(x, a+b)