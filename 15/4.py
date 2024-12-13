for a in range(1000):
    fl = 1
    for x in range(100):
        for y in range(100):
            if not((x + 2 * y < a) or (y > x) or (x > 60)):
                fl = 0
    if fl:
        print(a)