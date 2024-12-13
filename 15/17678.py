for a in range(1000):
    fl = 1
    for x in range(100):
        for y in range(100):
            if (((x + y) <= 24) or (y <= (x - 2)) or (y >= a)) == 0:
                fl = 0
    if fl:
        print(a) # 12