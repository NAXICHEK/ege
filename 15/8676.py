for a in range(1000):
    fl = 1
    for x in range(100):
        if (((x&500 != 0) and (x&200 == 0)) <= (not(x&a == 0))) == 0:
            fl = 0
    if fl:
        print(a)
        break