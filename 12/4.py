for i in range(4, 100):
    s = '3' + '5' * i
    while '25' in s or '355' in s or '555' in s:
            s = s.replace('25', '3', 1)
            s = s.replace('355', '52', 1)
            s = s.replace('555', '23', 1)
    if sum(map(int, s)) == 27:
        print(i, s)