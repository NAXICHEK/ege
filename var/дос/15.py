for a in range(100):
    fl = 1
    for x in range(1000):
        for y in range(1000):
            if ((5 < y) or (x > 32) or (x + 2*y < a)) == 0: fl = 0
    if fl:
        print(a)
        break