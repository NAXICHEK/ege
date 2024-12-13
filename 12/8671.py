for i in range(4, 10001):
    s = '4' + '6' * i
    while '46' in s or '666' in s:
        s = s.replace('46', '5', 1)
        s = s.replace('666', '4', 1)
    if sum(map(int, s)) > 1000:
        print(i) # 791
        break