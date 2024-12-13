for i in range(4, 10000):
    s = '5' + '2' * i
    while '52' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '11')
        s = s.replace('2222', '5')
        s = s.replace('1122', '25')
    if sum(map(int, s)) == 64:
        print(i)#56