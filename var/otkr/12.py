for i in range(4, 10000):
    s = '1' + '9'*i
    while '19' in s or '399' in s or '999' in s:
        s = s.replace('19', '9', 1)
        s = s.replace('399', '91', 1)
        s = s.replace('999', '3', 1)
    if sum(map(int, s)) == 33:
        print(i)