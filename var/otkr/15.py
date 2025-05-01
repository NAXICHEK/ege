for a in range(1, 100):
    fl = 'aboba'
    for x in range(1000):
        if (((x & 52 != 0) and (x & 48 == 0)) <= (not(x & a == 0))) == 0:
            fl = 'DJ Arbuz'
    if fl == 'aboba':
        print(a)