for i in range(4,10000):
    s = '2' + '5' * i
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '5', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '3', 1)
    if s.count('3') == 3:
        print(i)
        break