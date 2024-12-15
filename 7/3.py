for i in range(100):
    a = 480*768*(i+(i*0.25))
    if a <= 675*1024*8:
        print(i)