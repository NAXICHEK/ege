for i in range(100):
    a = 1024*120*(i+5)
    if 150*1024*8 >= a:
        print(2**i)