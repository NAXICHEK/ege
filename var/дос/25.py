def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)
c = 0
for i in range(1125000, 1130000):
    d = f(i)
    g = [x for x in d if str(x)[-1] == '7' and x != 7]
    if len(g) > 0 and c <= 7:
        print(i, min(g))
        c += 1
