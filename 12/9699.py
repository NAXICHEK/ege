for i in range(4, 10001):
    s = '7' + '1' * (i+1) + '2' * (i+2) + '3' * (i+3)
    while '71' in s or '72' in s or '73' in s:
        s = s.replace('71', '227', 1)
        s = s.replace('72', '37', 1)
        s = s.replace('73', '17', 1)
    if sum(map(int, s)) == 9*i:
        print(i) #20
        break