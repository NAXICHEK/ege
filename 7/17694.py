for i in range(1000): # 256
    a = 600*400 * i
    if i % 8 == 0:
        if a <= 350 * 1024 * 8:
            print(2**i)