for a in range(1000):
    fl = 1
    for x in range(100):
        for y in range(100):
            if ((x < a) or (y < a) or (x + y*2 > 50)) == 0:
                fl = 0
    if fl:
        print(a) # 17
        break