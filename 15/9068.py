for a in range(1000):
    fl = 1
    for x in range(100):
        for y in range(100):
            if ((x >= 27) or (2*x < 3*y) or (((2+x) * (y-3)) < a)) == 0:
                fl = 0
    if fl:
        print(a)
        break