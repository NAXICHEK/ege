for a in range(1000):
    fl = 1
    for x in range(100):
        for y in range(100):
            if ((x + 2*y < a) or (y < x) or (y > 60)) == 0:
                fl = 0
    if fl:
        print(a)
        break