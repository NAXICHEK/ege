for i in range(100):
    a = (1600*1200 * i)/5
    if (a+(100*1024*8)) <= (10*1024*1024*8)/32:
        print(i)