for i in range(1000):
    a = (2560 * 1440 * i)/(4/3)
    if a <= 4 * 1024 * 1024 * 8:
        print(2**i) # 4096