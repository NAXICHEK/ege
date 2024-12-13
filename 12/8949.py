for i in range(4, 10001):
    s = '2' + '5' * i
    while '25' in s or '35' in s or '555' in s:
        s = s.replace('25', '53', 1)
        s = s.replace('35', '2', 1)
        s = s.replace('555', '23', 1)
    if sum(map(int, s)) % 7 == 0:
        print(i) # 21
        break