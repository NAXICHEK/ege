def f(x, y):
    return x % y == 0

for a in range(1000):
    fl = 1
    for x in range(1000):
        if (((f(x, 10)) and (f(x, 26)) and (x >= 300)) <= (a <= x)) == 0:
            fl = 0
    if fl:
        print(a)