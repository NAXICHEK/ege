for i in range(4, 10000):
    s = '3' + '9' * i + '5' * i
    while '39' in s or '35' in s or '555' in s:
        s = s.replace('39', '55', 1)
        s = s.replace('35', '9', 1)
        s = s.replace('555', '3', 1)
    if sum(map(int, s)) % len(s) == i:
        print(i)