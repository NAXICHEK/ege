def f(a, x, b):
    return a <= x <= b

for a in range(1000):
    fl = 0
    for x in range(100):
        if (((not f(5, x, 54)) and (f(50, x, 93))) <= (x > a)) == 0:
            fl += 1
    if fl == 20:
        print(a)