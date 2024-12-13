def div(x):
    d = set()
    for i in range(2, int(x ** 0.5 + 1)):  # если не нужно включать само число, то в рендже вместо 1 ставим 2
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for i in range(400000001, 400100001):
    d = div(i)
    if len(d) >= 5:
        a = d[0] * d[1] * d[2] * d[3] * d[4]

        if str(a)[-2:] == '17' and a < i:
            print(a, d[4])