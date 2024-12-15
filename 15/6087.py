promejutok = lambda a, x, b: a <= x <= b
for a in range(1000):
    fl = 1
    for x in range(1000):
        if (promejutok(15, x, 40) <= (((not promejutok(21, x, 63)) and (not promejutok(7, x, a))) <= (not promejutok(15, x, 40)))) == 0:
            fl = 0
    if fl:
        print(a)
