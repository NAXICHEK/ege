def f(x, y):
    return str(x)[0] == str(y)[0]

for a in range(100):
    fl = 1
    for x in range(1, 1000):
        if ((not(f(x, 28)) and f(x, 47)) <= (x > a - 20)) != 1:
            fl = 0
            break
    if fl:
        print(a)