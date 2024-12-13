for a in range(1000):
    fl = 1
    for x in range(100):
        for y in range(100):
            if ((x * y < a) or (x < y) or (9 < x)) == 0:
                fl = 0
    if fl:
        print(a)
        break # 82