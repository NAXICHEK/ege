def f(x, y):
    return x % y == 0

for a in range(1, 1000):
    fl = 1
    for x in range(1, 1000):
        if (not(f(x, 17)) or (not(f(x, 12)))) <= (not (f(x, a))):
            fl = 0
    if fl:
        print(a)