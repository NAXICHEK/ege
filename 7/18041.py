for i in range(100000):
    a = 3840 * 2160 * i
    if a <= 25600*60*60*2:
        if i % 8 == 0:
            print(2**i) # 65536