for i in range(10000, 100000):
    i = str(i)
    a = i[0] + i[2] +i[4]
    b = i[1] + i[3]
    a = int(a)
    b = int(b)
    c = str(min(a, b)) + str(max(a, b))
    if c == '621':
        print(i)