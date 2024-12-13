for i in range(4, 10001):
    s = '5' + '2' * i
    while '72' in s or '522' in s or '2222' in s:
        s = s.replace('72', '2', 1)
        s = s.replace('522', '27', 1)
        s = s.replace('2222', '5', 1)
    if sum(map(int, s)) == 63:
        print(i) #186
        break