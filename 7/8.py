c = 0
for x in range(1, 10000000):
    for y in range(1, 10000000):
        a = x*600 * y*600 * 24
        if a <= 12*1024*1024*8:
            print(x, 'x')
            print(y, 'y')
            print(a, 'a', 12*1024*1024*8)
print((11*150*1*150*8)/1024/1024/8) # блять залупа