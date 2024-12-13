def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for i in range(1204300, 1204380 + 1):
    d = [int(g) for g in div(i) if g % 2 == 0]
    a = sum(d)
    if a != 0 and a % 10 == 0:
        print(i, a)