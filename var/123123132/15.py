for a in range(100):
    fl = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x - 3*y < a) or (y > 400) or (x > 56)) == 0:
                fl = 0
                break
    if fl:
        print(a)
