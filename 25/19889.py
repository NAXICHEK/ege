def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for i in range(902714, 1000000000):
    d = div(i)
    a = set()
    for j in d:
        if str(j)[-1] == '5' and j != 5:
            a.add(j)
    if a:
        print(i, min(a))