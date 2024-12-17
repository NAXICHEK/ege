for i in range(1000):
    a = 4096*1536 * i
    if a <= 7126 * 1024 * 8:
        print(2**i)