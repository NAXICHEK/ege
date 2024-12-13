for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if str(b*c) + str(a*b) == '621':
        print(i)