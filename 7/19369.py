for i in range(100000):
    a = 3840*2160 * 24
    if a*1326923 <= i*(32*1024*1024*1024*8):
        print(i)
        break