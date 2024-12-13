def f(x, y):
    return x % y == 0

for a in range(1000):
    fl = 1
    for x in range(1, 100):
        if ((a + x < 123) <= (f(x, 5) <= (not f(x,7)))) == 0:
            fl = 0
    if fl:
        print(a)
        break # 88