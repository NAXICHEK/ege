def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
c = 0
for i in range(500000, 200000, -1):
    d = [int(x) for x in div(i) if p(x)]
    s = sum(d)
    if s != 0 and s % 10 == 0 and c != 7:
        print(i, s)
        c += 1 # счетчик чтобы вывести 7 чисел