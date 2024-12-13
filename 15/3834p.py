for a in range(1, 1000):
    flag = 1
    for x in range(1, 10000):
        f = (a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))
        if f == 0:
            flag = 0
            break
    if flag == 1:
        print(a)
