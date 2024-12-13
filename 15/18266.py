for a in range(100):
    fl = 1
    for x in range(1, 100):
        if not((x&57 == 0) or ((x&23== 0) <= (not(x&a == 0)))):
            fl = 0
    if fl:
        print(a) # 40