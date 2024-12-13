for a in range(1, 101):
    fl = 0
    for x in range(90, 101):
        if not(x%79 == 0) and (x%31 == 0 <= (not(x%a == 0))) == 0:
            fl = 1
            break
    if fl == 0:
        print(a)