for i in range(200000000):
    a = i * 24
    if a <= 12*1024*1024*8:
        print(i)
        print((i*16)/1024/1024/8) # 8